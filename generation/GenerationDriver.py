from stylegan2.pretrained_networks import *
import numpy as np

class GenerationDriver:
    def __init__(self, MODEL_PATH):
        self.MODEL_PATH = MODEL_PATH

    def load_model(network_pkl):
        return load_networks(network_pkl)

    def seed2vec(Gs, seed):
        rnd = np.random.RandomState(seed)
        return rnd.randn(1, *Gs.input_shape[1:])

    def init_random_state(Gs, seed):
        rnd = np.random.RandomState(seed) 
        noise_vars = [var for name, var in Gs.components.synthesis.vars.items() if name.startswith('noise')]
        tflib.set_vars({var: rnd.randn(*var.shape.as_list()) for var in noise_vars}) # [height, width]

    def generate_image(Gs, z, artist, genre, style, truncation_psi=1.0):
        # Render images for dlatents initialized from random seeds.
        Gs_kwargs = {
            'output_transform': dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=True),
            'randomize_noise': False
        }
        if truncation_psi is not None:
            Gs_kwargs['truncation_psi'] = truncation_psi

        l1 = np.zeros((1,167))
        l1[0][artist] = 1
        l1[0][genre] = 1
        l1[0][style] = 1
        images = Gs.run(z, l1, **Gs_kwargs) # [minibatch, height, width, channel]
        return images[0]