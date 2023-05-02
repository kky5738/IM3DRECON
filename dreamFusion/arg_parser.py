class ArgParser():
    def __init__(
        self,
        text=None,
        negative='',
        O=None,
        O2=True,
        test=False,
        eval_interval=1,
        workspace='workspace',
        guidance='stable-diffusion',
        seed=None,
        image=None,
        known_view_interval=2,
        guidance_scale=100.0,
        save_mesh=None,
        mcubes_resolution=256,
        decimate_target=5e4,
        dmtet=True,
        tet_grid_size=128,
        init_ckpt='',
        iters=10000,
        lr=1e-3,
        ckpt='latest',
        cuda_ray=False,
        taichi_ray=False,
        max_steps=1024,
        num_steps=64,
        upsample_steps=32,
        update_extra_interval=16,
        max_ray_batch=4096,
        warmup_iters=2000,
        jitter_pose=False,
        uniform_sphere_rate=0.0,
        grad_clip=-1.0,
        grad_clip_rgb=-1.0,
        bg_radius=1.4,
        density_activation='softplus',
        density_thresh=0.1,
        blob_density=10.0,
        blob_radius=0.5,
        backbone='grid',
        optim='adan',
        sd_version='2.1',
        hf_key=None,
        w=64,
        h=64,
        known_view_scale=1.5,
        known_view_noise_scale=2e-3,
        dmtet_reso_scale=8.0,
        bound=1.0,
        dt_gamma=0.0,
        min_near=0.01,
        radius_range=[1.0, 1.5],
        theta_range=[45, 105],
        phi_range=[-180, 180],
        fovy_range=[40,80],
        default_radius=1.2,
        default_theta=90,
        default_phi=0,
        default_fovy=60,
        angle_overhead=30.0,
        angle_front=60.0,
        t_range=[0.02, 0.98],
        lambda_entropy=1e-3,
        lambda_opacity=0.0,
        lambda_orient=1e-2,
        lambda_tv=0.0,
        lambda_wd=0.0,
        lambda_mesh_normal=0.5,
        lambda_mesh_laplacian=0.5,
        lambda_guidance=1.0,
        lambda_rgb=10.0,
        lambda_mask=5.0,
        lambda_normal=0.0,
        lambda_depth=0.1,
        lambda_2d_normal_smooth=0.0,
        gui=None,
        H=800,
        W=800
    ) -> None:
        self.text=text
        self.negative=negative
        self.O=O
        self.O2=O2
        self.test=test
        self.eval_interval=eval_interval
        self.workspace= workspace
        self.guidance=guidance
        self.seed=seed
        
        self.image = image
        self.known_view_interval=known_view_interval
        self.guidance_scale=guidance_scale
        
        self.save_mesh=save_mesh
        self.mcubes_resolution=mcubes_resolution
        self.decimate_target=decimate_target
        
        self.dmtet=dmtet       
        self.tet_grid_size=tet_grid_size
        self.init_ckpt=init_ckpt
        
        ### training options
        self.iters=iters
        self.lr=lr
        self.ckpt=ckpt
        self.cuda_ray=cuda_ray
        self.taichi_ray=taichi_ray
        self.max_steps=max_steps
        self.num_steps=num_steps
        self.upsample_steps=upsample_steps
        self.update_extra_interval=update_extra_interval
        self.max_ray_batch=max_ray_batch
        self.warmup_iters=warmup_iters
        self.jitter_pose=jitter_pose        
        self.uniform_sphere_rate=uniform_sphere_rate
        self.grad_clip=grad_clip
        self.grad_clip_rgb=grad_clip_rgb
        
        ### 
        self.bg_radius=bg_radius
        self.density_activation=density_activation
        self.density_thresh=density_thresh
        self.blob_density=blob_density
        self.blob_radius=blob_radius
        self.backbone=backbone
        self.optim=optim
        self.sd_version=sd_version
        self.hf_key=hf_key
        self.w=w
        self.h=h
        self.known_view_scale=known_view_scale
        self.known_view_noise_scale=known_view_noise_scale
        self.dmtet_reso_scale=dmtet_reso_scale
        self.bound=bound
        self.dt_gamma=dt_gamma
        self.min_near=min_near
        self.radius_range=radius_range
        self.theta_range=theta_range
        self.phi_range=phi_range
        self.fovy_range=fovy_range
        self.default_radius=default_radius
        self.default_theta=default_theta
        self.default_phi=default_phi
        self.default_fovy=default_fovy
        self.angle_overhead=angle_overhead
        self.angle_front=angle_front
        self.t_range=t_range
        self.lambda_entropy=lambda_entropy
        self.lambda_opacity=lambda_opacity
        self.lambda_orient=lambda_orient
        self.lambda_tv=lambda_tv
        self.lambda_wd=lambda_wd
        self.lambda_mesh_normal=lambda_mesh_normal
        self.lambda_mesh_laplacian=lambda_mesh_laplacian
        self.lambda_guidance=lambda_guidance
        self.lambda_rgb=lambda_rgb
        self.lambda_mask=lambda_mask
        self.lambda_normal=lambda_normal
        self.lambda_depth=lambda_depth
        self.lambda_2d_normal_smooth=lambda_2d_normal_smooth
        self.gui=gui
        self.H=H
        self.W=W