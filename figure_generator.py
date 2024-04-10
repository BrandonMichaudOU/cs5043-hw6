import numpy as np
import matplotlib.pyplot as plt
import pickle


def scatter_accuracies():
    # Load accuracies from results files
    gru_test_accuracy = np.empty(5)
    mha_test_accuracy = np.empty(5)
    for r in range(5):
        with open(f'results/gru_grus_200_100_gact_tanh_dense_128_64_dact_elu_gc_0.001000_md_0.001000_lrate_0.000100_'
                  f'rot_{r}_results.pkl', "rb") as fp:
            results = pickle.load(fp)
            gru_test_accuracy[r] = results['predict_testing_eval'][1]
        with open(f'results/mha_nheads_8_kdims_8_dense_128_64_dact_elu_gc_0.001000_md_0.001000_lrate_0.000100_'
                  f'rot_{r}_results.pkl', "rb") as fp:
            results = pickle.load(fp)
            mha_test_accuracy[r] = results['predict_testing_eval'][1]

    # Make scatter plot of accuracies
    fig = plt.figure()
    for i in range(5):
        plt.scatter(gru_test_accuracy[i], mha_test_accuracy[i], label=f'Rotation {i}')
    plt.legend()
    plt.xlabel('GRU Accuracy')
    plt.ylabel('MHA Accuracy')
    plt.title('Model Accuracy')
    plt.axis('square')
    fig.savefig('figures/model_accuracies.png')


def scatter_epochs():
    # Load epochs. Hard-coded because I forgot to save to pkl file. Values taken from wandb
    gru_epochs = [322, 398, 424, 389, 172]
    mha_epochs = [67, 28, 21, 32, 41]

    # Make scatter plot of epochs
    fig = plt.figure()
    for i in range(5):
        plt.scatter(gru_epochs[i], mha_epochs[i], label=f'Rotation {i}')
    plt.legend()
    plt.xlabel('GRU Epochs')
    plt.ylabel('MHA Epochs')
    plt.title('Model Epochs')
    plt.axis('square')
    fig.savefig('figures/model_epochs.png')


if __name__ == '__main__':
    scatter_accuracies()
    scatter_epochs()
