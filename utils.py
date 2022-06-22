class plotImages():
    '''Plot "N" number of images for the given train/valid/test dataset'''
    def __init__(self, data:datasets, N:int=32) -> None:
        self.N = N
        self.data = data

    def plot_images(self) -> None:
        len_data = len(self.data)
        samples = self.generate_samples(len_data)

        rows = math.ceil(np.sqrt(self.N))
        cols = math.ceil(np.sqrt(self.N))

        fig = plt.figure()
        for i in range(self.N):
            ax = fig.add_subplot(rows, cols, i+1)
            ax.imshow(samples[i].view(28,28).cpu().numpy())
            ax.axis('off')

    def generate_samples(self, len_data:int) -> List[torch.Tensor]:
        sample_indexes = random.sample(range(len(self.data)), self.N)
        return [image for image, label in [self.data[i] for i in sample_indexes]]


class packageVersion:
  ''' Find the version of the Package passed as parameter'''
    def __call__(self, *args):
        for arg in args:
            print(arg.__version__)

#Sleeper util for colab
import time
def sleep_jupyter(x = 100):
    time.sleep(x)
    print("yes")
while True:
    sleep_jupyter()
