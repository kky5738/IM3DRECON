# IM3DRECON
Final project part for image to 3D reconstruction

Text to 3D 프로젝트 중 3D reconstruction 관련 논문 repo 클론 및 공부한 내용 업로드



## Dreamfusion(작성 중)
Poole, B., Jain, A., Barron, J. T., & Mildenhall, B. (2022). Dreamfusion: Text-to-3d using 2d diffusion. arXiv preprint arXiv:2209.14988.

Text to 3D reconstruction의 새로운 approach를 제시한 논문.

(text, 3D) pair로 구성된 데이터 셋이 부족하여 text conditioning 3D Diffusion 모델을 학습시키기 어려움.

그 대안으로 2D diffusion과 NeRF를 이용해 text로 3D object를 합성(생성)하는 방법 제시.
1. latent diffusion 모델에 text를 넣어 2D image 생성
2. 2D image를 이용해 NeRF 모델을 optimize
3. NeRF를 optimize할 때 SDS Loss라는 새로운 Loss 제시
