import matplotlib.pyplot as plt

class VolumeHistogram:
    def __init__(self, volumes, bars):
        self.volumes = volumes
        self.bars = bars

    def plot(self):
        plt.bar(self.bars, self.volumes)
        plt.xlabel('Bars')
        plt.ylabel('Volume')
        plt.title('Volume Quantity on Histogram Bars')
        for i, v in enumerate(self.volumes):
            plt.text(self.bars[i], v, str(v), ha='center', va='bottom')
        plt.show()
