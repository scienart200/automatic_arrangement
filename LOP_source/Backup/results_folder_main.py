#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

# Main script for processing results folders
# Processing consists in :
#   per folder processing :
#       - generating midi
#       - plot model weights
#   "global" processing
#       - write result.csv files, which sums up and sort the results of the different hyper-parameter configurations
#       - plot hyper-parameter statistics
#
#
#
#
# IMPORTANT :
#   To avoid mixing training and generation files, and most importantly to be sure that the reconstruction is correctly done,
#   USE EXACTLY THE SAME DATA FOLDER THAT THE ONE USED FOR training
#   Hence, if trained on guillimin, scp it before doing any post processing


import glob
import logging

from results_folder_generate import generate_midi, generate_midi_full_track_reference
from results_folder_plot_weights import plot_weights
from results_folder_csv import get_results_and_id, write_csv_results
from corrupted import generate_corrupted_results
from clean_result_folder import clean

############################################################
# Logging
############################################################
log_file_path = 'log/generate_log'
# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=log_file_path,
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)


def processing_results(configurations_path, data_folder, track_paths, generation_length=200, seed_size=20):
    # path has to be the roots of the results folders
    # e.g. : /home/aciditeam-leo/Aciditeam/lop/Results/event_level/discrete_units/quantization_4/gradient_descent/LSTM

    ############################################################
    # Processing
    ############################################################
    # Get folders starting with a number
    configurations = glob.glob(configurations_path + '/[0-9]*')
    id_result_list = []
    number_of_version = 5

    for configuration in configurations:
        # generate_midi(configuration, data_folder, generation_length, seed_size, None, logging)
        for track_path in track_paths:
            generate_midi_full_track_reference(configuration, data_folder, track_path, seed_size, number_of_version, logging)
        # generate_corrupted_results(configuration, data_folder, generation_length, seed_size)
        # plot_weights(configuration, logger_plot)
        # id_result_list.append(get_results_and_id(configuration))

    # write_csv_results(configurations_path, id_result_list, configurations[0])
    # plot_hparam_curves(configurations_path)


if __name__ == '__main__':
    ####################################################################################
    ####################################################################################
    ####################################################################################
    # IMPORTANT :
    #   To avoid mixing training and generation files, and most importantly to be sure that the reconstruction is correctly done,
    #   USE EXACTLY THE SAME DATA FOLDER THAT THE ONE USED FOR training
    #   Hence, if trained on guillimin, scp the database folder before doing any post processing
    ####################################################################################
    ####################################################################################
    ####################################################################################

    data_folder = '/home/aciditeam-leo/Aciditeam/lop/Results_guillimin/27_02_17/Results/event_level/binary/quantization_100/Data'
    model_path = '/home/aciditeam-leo/Aciditeam/lop/Results_guillimin/27_02_17/Results/event_level/binary/quantization_100/gradient_descent'
    track_paths = [
        '/home/aciditeam-leo/Aciditeam/database/Orchestration/LOP_database_29_05_17/liszt_classical_archives/16',
        '/home/aciditeam-leo/Aciditeam/database/Orchestration/LOP_database_29_05_17/bouliane/22',
        '/home/aciditeam-leo/Aciditeam/database/Orchestration/LOP_database_29_05_17/bouliane/3',
        '/home/aciditeam-leo/Aciditeam/database/Orchestration/LOP_database_29_05_17/bouliane/0',  # This one is in train set
    ]

    # data_folder = "/home/crestel/lop/Data"
    # model_path = "/sb/project/ymd-084-aa/Results/event_level/discrete_units/quantization_4/gradient_descent"
    # track_paths = [
    #     '/home/crestel/database/orchestration/liszt_classical_archive/16',
    #     '/home/crestel/database/orchestration/bouliane/22'
    # ]

    #################################
    # Generate the results for all the configs of a model
    #################################
    # for nn in ['cRBM', 'FGcRBM', 'RBM_inpainting']:
    #     model_path_this = model_path + '/' + nn
    #     clean(model_path_this)
    #     processing_results(model_path_this, data_folder, track_paths)

    #################################
    # Or just generate or plot weight of a specific configuration
    #################################
    configurations = [
        "/home/aciditeam-leo/Aciditeam/lop/Results/event_level/binary/quantization_100/adam_L2/FGgru/11",
        "/home/aciditeam-leo/Aciditeam/lop/Results/event_level/binary/quantization_100/adam_L2/FGgru/12",
        ]
    data_folder = "../Data"
    generation_length = 50
    corruption_flag = None
    number_of_version = 5

    for configuration in configurations:
        plot_weights(configuration, logging)
        generate_midi(configuration, data_folder, generation_length, corruption_flag, logging)
        for track_path in track_paths:
            generate_midi_full_track_reference(configuration, data_folder, track_path, number_of_version, logging)