#Câu 1 tự luận
#1. Viết function thực hiện đánh giá classification model bằng F1-Score.
def evaluate_classification_model(tp, fp, fn):
    # Kiểm tra kiểu dữ liệu của các giá trị đầu vào
    if not isinstance(tp,int):
        print('tp must be int')
        return
    if not isinstance(fp,int):
        print ('fp must be int')
        return
    if not isinstance (fn,int):
        print ('fn mustb be int')
        return
     
    # Kiểm tra giá trị của các biến đầu vào phải lớn hơn 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return
    
    # Tính toán Precision
    precision = tp / (tp + fp)
    
    # Tính toán Recall
    recall = tp / (tp + fn)
    
    # Tính toán F1-Score
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    # In ra kết quả
    print(f"Precision: {precision:.2f}")
    # cấu trúc {ten bien:.2f}- .2f dinh dang 2 so le
    print(f"Recall: {recall:.2f}")
    print(f"F1-Score: {f1_score:.2f}")

# Ví dụ sử dụng hàm với các giá trị TP, FP, FN
evaluate_classification_model(tp=2, fp=4, fn=5)
