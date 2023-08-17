# Realfusion 코드 공부
Melas-Kyriazi, L., Laina, I., Rupprecht, C., & Vedaldi, A. (2023). Realfusion: 360deg reconstruction of any object from a single image. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 8446-8455).

main.py 파일은 기본적으로 리눅스 command line을 통해 실행
+ line 1~23: pytorch, math, numpy, custom class 등의 필요한 모듈 import

25 line에 정의된 main 함수는 다음과 같은 실행 과정을 거침
1. command line에서 입력받은 실행 옵션 및 함수 인자들을 Options().parse_args()를 통해 parsing
2. seed_everything() 함수를 통해 랜덤 시드 고정
3. NeRF backbone으로 Instant-NGP 모델 불러옴
4. device(GPU or CPU) 지정
5. custom dataset 객체를 통해 train, validation, text loader 생성
6. opt.test: bool 인자를 통해 trian/test 모드 지정
7. 