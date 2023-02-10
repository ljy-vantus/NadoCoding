import cv2

cap = cv2.VideoCapture('data/video.mp4')

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) * 2

out = cv2.VideoWriter('data/output_fast.mp4', fourcc, fps, (width, height))
# 저장 파일명, 코덱, FPS, 크기(width, height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    out.write(frame) # 영상데이터만 저장 (소리 X)
        
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break
        
out.release()    
cap.release()
cv2.destroyAllWindows()