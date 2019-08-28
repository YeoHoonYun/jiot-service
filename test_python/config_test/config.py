import configparser

config = configparser.ConfigParser()
config.read('.\config')

config_main = config["MAIN"]
print(config_main)

project_root_path = config_main['project_root']
print(project_root_path)

process_list = config.get("PROCESS", "processes").split(" ")
print(process_list)

main = config.get("MAIN", "db_port")
print(type(main))