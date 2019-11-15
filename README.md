# Hannibal_ERC2019

- Thi 2 vòng.
- Vòng 1 trong 17-28/11.
- Bài toán là supervised classification.
- Train set (handout) gồm ~5000 cặp (file .pcm - file âm thanh/ tiếng nói, label). Label là 1 trong 6 cảm xúc: happy, sad, anger, fear, disgust, và neutral (vui, buồn, giận, sợ, kinh tởm, trung tính).
- Test set (public-test) gồm ~1000 files âm thanh (ko có label).
- Mỗi ngày được submit 3 lần.
- Vòng 2 thì chỉ là chọn mấy đội top lên present rồi train lại trên server của BTC, với test lại trên ~1000 files closed-test khác. 

More info:
1. File audio chỉ là một câu nói ngắn.
2. Học trực tiếp từ tín hiệu âm thanh, phân tích ngữ điệu.
3. Thầy Nam gợi ý dùng bộ lọc feature là MFCC.
4. Dữ liệu tiếng anh.

Task #1:
- Thanh: tập trung trả lời câu hỏi là cái feature vector của nó trả về sẽ chứa những thông tin gì.
- Việt: chú ý phần cài đặt cụ thể và những tham số liên quan mà mình có thể điều chỉnh lúc dùng thuật toán (ý là cái hàm trong thư viện) đó.
- Tiến: tìm hiểu về các bộ dữ liệu phổ biến có sẵn, coi qua về toàn bộ các bước phía sau... xem ngta dùng thuật toán học gì.

Meeting #1: chiều thứ 7.

Some links:
https://www.researchgate.net/profile/Manikrao_Dhore/publication/43785303_Speech_Emotion_Recognition_Using_Support_Vector_Machines/links/0deec5243c08426014000000.pdf
https://www.academia.edu/6784167/c%C3%A1c_vector
https://pdfs.semanticscholar.org/05ba/884878eaff5f977d488fe792f78e57e18418.pdf
https://github.com/amanbasu/speech-emotion-recognition
