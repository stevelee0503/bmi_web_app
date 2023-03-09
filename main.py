import matplotlib.pyplot as plt
import matplotlib
import gradio as gr

matplotlib.use("Agg")

# 비만의 정도
obesity_level = (("저체중", "Underweight", "blue"), ("정상", "Normal weight", "green"), ("비만 전단계", "Pre obesity", "yellow"),
                 ("1단계 비만", 'Obesity class I', "orange"), ("2단계 비만", "Obesity class II", "red"),
                 ("3단계 비만", "Obesity class III", "purple"))


def calculate_bmi(height: float, weight: float):
    """
    BMI 지수와 비만의 정도를 계산하는 함수.
    인자: 키(height, m), 몸무게(weight, kg)
    반환값: (BMI 지수, 비만의 정도, 비만의 정도 그래프)
    """
    bmi = round(weight / (height ** 2), 1)
    if bmi < 18.5:
        obesity = obesity_level[0]
    elif bmi < 25:
        obesity = obesity_level[1]
    elif bmi < 30:
        obesity = obesity_level[2]
    elif bmi < 35:
        obesity = obesity_level[3]
    elif bmi < 40:
        obesity = obesity_level[4]
    else:
        obesity = obesity_level[5]

    # 비만의 정도 그래프 생성
    fig, ax = plt.subplots()
    ax.bar(obesity[1], bmi, color=obesity[2])
    ax.set_ylim(0, 50)
    ax.set_xlabel("Obesity Level")
    ax.set_ylabel("BMI")
    ax.set_title("BMI and Obesity Level")

    return str(bmi), obesity[0], fig


# 입력값을 받을 입력 인터페이스 정의
input_interface = [
    gr.inputs.Slider(minimum=1.0, maximum=2.5, default=1.6, label="키 (m)"),
    gr.inputs.Slider(minimum=30.0, maximum=150.0, default=60.0, label="몸무게 (kg)")
]

# 출력값을 보여줄 출력 인터페이스 정의
output_interface = [
    gr.outputs.Textbox(label="BMI 지수"),
    gr.outputs.Textbox(label="비만의 정도"),
    gr.Plot(label="비만의 정도 그래프")
]

# 인터페이스와 함수를 연결하여 웹앱 생성
app_interface = gr.Interface(
    fn=calculate_bmi,
    inputs=input_interface,
    outputs=output_interface,
    title="BMI 계산기"
)

app_interface.launch()
