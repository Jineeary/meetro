<!---
Bản quyền 2020 The HuggingFace Team. Bảo lưu mọi quyền.

Tài liệu này được cấp phép theo Giấy phép Apache, Phiên bản 2.0 (sau đây gọi là "Giấy phép"). Trừ khi được quy định trong Giấy phép, bạn không được phép sử dụng tài liệu này. Bạn có thể xem bản sao của Giấy phép tại liên kết dưới đây:

    http://www.apache.org/licenses/LICENSE-2.0

Trừ khi pháp luật yêu cầu hoặc có thỏa thuận bằng văn bản, phần mềm phân phối theo Giấy phép này được cung cấp "NGUYÊN TRẠNG", KHÔNG CÓ BẢO HÀNH hay ĐIỀU KIỆN nào, dù là rõ ràng hay ngụ ý. Hãy tham khảo Giấy phép để biết ngôn ngữ quy định về các quyền và hạn chế theo Giấy phép.
-->

<h1 align="center">
    <p>Meetro🚇: Lên kế hoạch gặp gỡ tại các ga tàu điện ngầm một cách dễ dàng</p>
</h1>

<p align="center">
    <a href="https://circleci.com/gh/huggingface/transformers"><img alt="Build" src="https://img.shields.io/circleci/build/github/huggingface/transformers/main"></a>
    <a href="https://github.com/huggingface/transformers/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/huggingface/transformers.svg?color=blue"></a>
    <a href="https://huggingface.co/docs/transformers/index"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/transformers/index.svg?down_color=red&down_message=offline&up_message=online"></a>
    <a href="https://github.com/huggingface/transformers/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/transformers.svg"></a>
    <a href="https://github.com/huggingface/transformers/blob/main/CODE_OF_CONDUCT.md"><img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg"></a>
    <a href="https://zenodo.org/badge/latestdoi/155220641"><img src="https://zenodo.org/badge/155220641.svg" alt="DOI"></a>
</p>

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_zh-hans.md">简体中文</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_zh-hant.md">繁體中文</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ko.md">한국어</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_es.md">Español</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ja.md">日本語</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_hd.md">हिन्दी</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ru.md">Русский</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_pt-br.md">Рortuguês</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_te.md">తెలుగు</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_fr.md">Français</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_de.md">Deutsch</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_vi.md">Tiếng Việt</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ar.md">العربية</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ur.md">اردو</a> |
    </p>
</h4>

<h3 align="center">
    <p>Nhấn vào hình ảnh dưới đây để truy cập trang web.</p>
    <a href="http://127.0.0.1:5500">
        <img src="https://github.com/Jineeary/meetro/blob/main/image/img_subway_modified.jpg" alt="Nhấn vào hình ảnh để truy cập trang web">
    </a>
</h3>

<h2 align="center">
    <p>Giải pháp tối ưu để tìm điểm gặp gỡ trung tâm!</p>
</h2>

## Tổng quan
Meetro là một dịch vụ web sáng tạo được thiết kế để đơn giản hóa việc tìm một địa điểm gặp gỡ trung tâm, đặc biệt là cho bạn bè hoặc nhóm sống rải rác khắp khu vực đô thị. Giải pháp của chúng tôi không chỉ tính toán ga tàu điện ngầm trung tâm mà còn gợi ý các điểm tham quan lân cận, xem xét mức độ phổ biến của các địa điểm để tạo ra trải nghiệm gặp gỡ thú vị hơn.

## Xác định và phân tích vấn đề
Đối với những người bạn sống ở nhiều nơi khác nhau, việc chọn một địa điểm gặp gỡ trung tâm có thể là thách thức. Các nền tảng hiện có như [WeMeetPlace](https://wemeetplace.com) và [Ya-manna](https://ya-manna.com) cũng cố gắng tìm điểm trung tâm, nhưng thường thiếu các điểm tham quan cập nhật hoặc mong muốn ở những khu vực đó. Meetro kết hợp tính toán điểm trung tâm với dữ liệu về các điểm tham quan hiện đại để cung cấp các điểm gặp gỡ thực tiễn và hấp dẫn.

### Cơ hội nghiên cứu và cải tiến
1. **WeMeetPlace** ([Trang web](https://wemeetplace.com) | [GitHub](https://github.com/we-meetting/weMeet-frontend))：  
   WeMeetPlace tập trung vào việc xác định điểm trung tâm, nhưng thiếu các điểm tham quan gần nhiều ga và thường sử dụng dữ liệu lỗi thời. Mục tiêu của chúng tôi là đảm bảo rằng Meetro cung cấp trải nghiệm dựa trên các điểm tham quan cập nhật và hấp dẫn.

2. **Ya-manna** ([Trang web](https://ya-manna.com) | [GitHub](https://github.com/mandooro/YaManNa))：  
   Ya-manna có bao gồm các tùy chọn giải trí, nhưng ưu tiên các điểm trung tâm chính xác, có thể thiếu các địa điểm phổ biến. Chúng tôi sẽ khắc phục điều này bằng cách tăng trọng số cho các điểm tham quan phổ biến, ngay cả khi chúng nằm ngoài một chút so với điểm trung tâm.

Bằng cách giải quyết những hạn chế này, Meetro cung cấp trải nghiệm phù hợp cho những người dùng muốn nhiều hơn là chỉ một điểm gặp gỡ, giúp họ dễ dàng tiếp cận các địa điểm thú vị với dữ liệu điểm tham quan cập nhật.

## Tên và thương hiệu dự án
**Meetro** được lấy từ “Meet” và “Metro”, thể hiện ý tưởng gặp nhau tại các ga tàu điện ngầm. Tên gọi nhấn mạnh vào việc cung cấp các điểm gặp gỡ thuận tiện và thú vị ở khu vực tàu điện ngầm.

## Tuyên bố sứ mệnh
“Sứ mệnh của chúng tôi là giúp bạn bè dễ dàng tìm thấy ga tàu điện ngầm hiệu quả nhất và các địa điểm gần đó để vui chơi. Dù là buổi gặp gỡ thông thường hay dịp đặc biệt, chúng tôi đơn giản hóa quá trình chọn điểm gặp gỡ hoàn hảo.”

- **Mục tiêu**: Phát triển một dịch vụ web để xác định ga tàu trung tâm lý tưởng và cung cấp các gợi ý về các điểm tham quan phổ biến gần đó.
- **Đối tượng người dùng mục tiêu**: Meetro được thiết kế dành cho bạn bè, gia đình hoặc nhóm muốn có cách dễ dàng, thú vị và hiệu quả để lên kế hoạch gặp nhau tại các vị trí trung tâm trong hệ thống tàu điện ngầm.

## Tính năng và chức năng
Hệ thống điểm số độc đáo của Meetro kết hợp tính toán điểm trung tâm với xếp hạng điểm tham quan, đảm bảo người dùng nhận được đề xuất về một ga tàu trung tâm có các địa điểm phổ biến lân cận để có một buổi gặp gỡ đáng nhớ.

### Các tính năng chính
- **Tính toán điểm trung tâm với phạm vi linh hoạt**: Thay vì một điểm trung tâm cố định, Meetro tính toán điểm trung tâm trong một phạm vi cho phép người dùng ưu tiên các ga có điểm tham quan gần đó.
- **Trọng số điểm tham quan**: Meetro gán trọng số cho các điểm tham quan. Các địa điểm thông thường có trọng số là 1, trong khi các điểm tham quan phổ biến (ví dụ như công viên giải trí, trung tâm thương mại) có trọng số là 3, giúp ưu tiên các địa điểm hấp dẫn.
- **Tính điểm cho ga tàu**: Mỗi ga tàu điện ngầm gần điểm trung tâm sẽ được tính điểm dựa trên khoảng cách và trọng số của điểm tham quan. Các ga xa điểm trung tâm sẽ có điểm số thấp hơn, trong khi các ga có điểm tham quan phổ biến sẽ nhận được điểm cao hơn.
- **Đề xuất tối ưu**: Meetro hiển thị cho người dùng ga tàu điện ngầm có điểm số cao nhất trong phạm vi điểm trung tâm, đảm bảo sự cân bằng giữa tính tiện lợi và niềm vui.

### Sự khác biệt: Điều gì khiến Meetro nổi bật
| Tính năng                           | WeMeetPlace / Ya-manna                  | Meetro                                     |
|-----------------------------------|-----------------------------------------|--------------------------------------------|
| **Tính toán điểm trung tâm**           | Điểm trung tâm cố định                          | Điểm trung tâm có các điểm tham quan phổ biến          |
| **Thông tin điểm tham quan**         | Giới hạn hoặc lỗi thời                     | Điểm tham quan hiện đại và phổ biến             |
| **Dung lượng dữ liệu**                    | Ít                                   | Dữ liệu phong phú hơn, bao gồm nhiều điểm tham quan hơn   |
| **Lựa chọn của người dùng**                   | Hạn chế                                 | Linh hoạt, dựa trên mức độ phổ biến và vị trí | 

Bằng cách sử dụng dữ liệu cập nhật và cung cấp các tùy chọn dựa trên mức độ phổ biến của các điểm tham quan, Meetro nâng cao trải nghiệm lập kế hoạch cuộc gặp gỡ vượt trội so với hiện tại.

## Công cụ và ngôn ngữ phát triển
Meetro được phát triển với bộ công nghệ mạnh mẽ để đảm bảo hiệu suất cao, khả năng mở rộng và giao diện thân thiện với người dùng.

- **Ngôn ngữ và khung**:
  - **JavaScript (Node.js)**: Xử lý logic backend và tích hợp API.
  - **Python**: Dùng để xử lý dữ liệu, tính trọng số điểm tham quan và tích hợp bản đồ.
  - **HTML/CSS**: Định nghĩa cấu trúc và thiết kế giao diện người dùng.
  - **JavaScript (React)**: Tạo giao diện động và tương tác tốt.
- **Công cụ**:
  - **GitHub**: Kiểm soát phiên bản để theo dõi tiến độ và hỗ trợ làm việc nhóm.
  - **OpenStreetMap (OSM)**: Cung cấp dữ liệu bản đồ mã nguồn mở đầy đủ.
  - **Google Maps API**: Hỗ trợ hiển thị bản đồ, tính toán điểm trung tâm và truy xuất dữ liệu điểm tham quan.
  - **Figma**: Công cụ hợp tác cho thiết kế UI/UX, đảm bảo tính nhất quán trong trải nghiệm người dùng.

## Trách nhiệm của nhóm
Để đảm bảo dự án hoạt động trơn tru, mỗi thành viên trong nhóm đều có vai trò được phân định rõ ràng:

- **Trưởng dự án**: Soo-bin Yoon – Giám sát phát triển và điều phối tổng thể dự án.
- **Quản lý mã nguồn**: Ye-eun Yeom – Quản lý kho mã nguồn và tích hợp mã.
- **Người thu thập dữ liệu**: Yeon-jin Kim – Thu thập và xử lý dữ liệu, đảm bảo tính chính xác của thông tin điểm tham quan.
- **Người tạo trang web**: Yeo-jin Kim – Thiết kế và phát triển giao diện trang web để cung cấp trải nghiệm người dùng liền mạch.

## Bắt đầu nhanh
Để bắt đầu sử dụng Meetro, nhấn vào liên kết dưới đây để truy cập trang web:

[Truy cập Meetro](http://localhost:3000)

## Hướng dẫn sử dụng
1. **Nhập vị trí**: Nhập vị trí của từng thành viên trong nhóm.
2. **Tìm điểm trung tâm**: Ứng dụng sẽ tính toán phạm vi điểm trung tâm và hiển thị các ga tàu điện ngầm gần đó.
3. **Xem đề xuất**: Các ga có điểm số cao nhất dựa trên mức độ gần gũi và mức độ phổ biến của các điểm tham quan sẽ được đề xuất làm nơi gặp gỡ.
Meetro giúp quá trình chọn điểm gặp gỡ trở nên dễ dàng hơn bằng cách cung cấp chức năng thân thiện và các gợi ý hữu ích.

## Đóng góp
Chúng tôi hoan nghênh các đóng góp để cải thiện Meetro. Để đóng góp, hãy làm theo hướng dẫn trong CONTRIBUTING.md. Các đóng góp có thể bao gồm cải tiến mã, tính năng mới hoặc cập nhật dữ liệu điểm tham quan.

## Giấy phép
Dự án này được cấp phép theo Giấy phép Apache 2.0. Xem tệp [LICENSE](https://github.com/Jineeary/meetro/blob/main/LICENSE) để biết thêm chi tiết.

## Các bản demo và ví dụ trực tuyến
Ngoài các chức năng chính, chúng tôi cung cấp các bản demo sau để giới thiệu khả năng của Meetro:

1. Demo tính toán điểm trung tâm: Hiển thị cách Meetro tính toán điểm trung tâm trong một phạm vi linh hoạt và đề xuất các ga.
2. Tính trọng số điểm tham quan: Hiển thị cách ưu tiên các địa điểm phổ biến dựa trên sở thích của người dùng.
3. Hành trình người dùng: Theo dõi một nhóm mẫu khi họ sử dụng giao diện Meetro để tìm nơi gặp gỡ tối ưu.
Khám phá Meetro ngay hôm nay để trải nghiệm cách gặp gỡ thông minh hơn!
