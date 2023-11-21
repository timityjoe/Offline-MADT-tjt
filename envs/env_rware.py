
from .rware.warehouse import Warehouse
# from .starcraft2.smac_maps import get_map_params

from .config_rware import get_config, get_rware_config
from .env_wrappers import ShareSubprocVecEnv

from loguru import logger
# logger.remove()
# logger.add(sys.stdout, level="INFO")
# logger.add(sys.stdout, level="SUCCESS")
# logger.add(sys.stdout, level="WARNING")

def make_eval_env(all_args, n_threads=1):
    def get_env_fn(rank):
        def init_env():
            if all_args.env_name == "RWARE":
                shelf_columns = all_args.shelf_columns
                column_height = all_args.column_height
                shelf_rows = all_args.shelf_rows
                num_agents = all_args.num_agents
                max_steps = all_args.max_steps
                # reward_type = RewardType.GLOBAL
                reward_type = all_args.reward_type
                layout = all_args.layout
                observation_type = all_args.observation_type

                msg_bits = 3
                sensor_range = 1
                request_queue_size = 5
                max_inactivity_steps = None

                env = Warehouse(shelf_columns, column_height, shelf_rows, 
                        num_agents, msg_bits, sensor_range, request_queue_size, 
                        max_inactivity_steps, max_steps, reward_type, layout, observation_type)
            else:
                print("Can not support the " + all_args.env_name + "environment.")
                raise NotImplementedError
            env.seed(all_args.seed * 50000 + rank * 10000)
            return env

        return init_env

    logger.info(f"n_threads:{n_threads}")
    return ShareSubprocVecEnv([get_env_fn(i) for i in range(n_threads)])


class Env:
    def __init__(self, n_threads=1):
        parser = get_config()
        parser_rware = get_rware_config()
        
        all_args = parser.parse_known_args()[0]
        all_args_rware = parser_rware.parse_args()

        logger.info(all_args)
        logger.info(all_args_rware)

        logger.info(f"n_threads:{n_threads}")
        self.real_env = make_eval_env(all_args_rware, n_threads)
        self.num_agents = all_args_rware.num_agents
        self.max_timestep = all_args_rware.max_steps
        self.n_threads = n_threads
