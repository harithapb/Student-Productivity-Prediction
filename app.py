import streamlit as st
import pickle
from PIL  import  Image
def main():
    model = pickle.load(open("productivity_model.sav", "rb"))
    scaler=pickle.load(open("scaler.sav","rb"))
    st.title("Student Productivity Prediction")
    st.subheader("Student Information")
    age = st.number_input("Age", min_value=10, max_value=100)
    gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    attendance = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0)
    st.subheader("Study Habits")
    study_hours = st.number_input("Study Hours per Day", min_value=0.0)
    focus = st.number_input("Focus Score", min_value=1, max_value=10)
    assignments = st.number_input("Assignments Completed", min_value=0)
    st.subheader("Lifestyle")
    sleep_hours = st.number_input("Sleep Hours", min_value=0.0)
    breaks = st.number_input("Breaks per Day", min_value=0)
    exercise = st.number_input("Exercise Minutes", min_value=0)
    st.subheader("Digital Usage")
    phone_usage = st.number_input("Phone Usage Hours", min_value=0.0)
    social_media = st.number_input("Social Media Hours", min_value=0.0)
    youtube = st.number_input("YouTube Hours", min_value=0.0)
    gaming = st.number_input("Gaming Hours", min_value=0.0)
    #breaks = st.number_input("Breaks per Day", min_value=0)
    st.subheader(" Other Factors")
    coffee = st.number_input("Coffee Intake (mg)", min_value=0)
    #exercise = st.number_input("Exercise Minutes", min_value=0)
    #assignments = st.number_input("Assignments Completed", min_value=0)
    #attendance = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0)
    stress = st.number_input("Stress Level", min_value=1, max_value=10)
    #focus = st.number_input("Focus Score", min_value=1, max_value=10)
    final_grade = st.number_input("Final Grade", min_value=0.0, max_value=100.0)
    if st.button('Predict Productivity'):
        if gender=='Female':
            gender_value=0
        elif gender == "Male":
            gender_value = 1
        else:
            gender_value = 2

        new_student = [[
            age,
            gender_value,
            study_hours,
            sleep_hours,
            phone_usage,
            social_media,
            youtube,
            gaming,
            breaks,
            coffee,
            exercise,
            assignments,
            attendance,
            stress,
            focus,
            final_grade
        ]]
        new_student_scaled = scaler.transform(new_student)

        prediction = model.predict(new_student_scaled)

        st.success(f"Predicted Productivity Score: {prediction[0]:.2f}")
        if prediction[0]>70:
            st.write("High productivity ")
        elif prediction[0]>=40:
            st.write("Medium productivity")
        else:
            st.write("Low productivity. Need attention")
        st.subheader('Personalized Recommendations')
        if study_hours<3:
            st.write('Your study hours are low.' '\n'
                     "Try a focused Pomodoro study session to gradually increase your study time."
                     )
            st.link_button(
                "Learn Pomodoro Technique",
                "https://todoist.com/productivity-methods/pomodoro-technique"
            )
        if phone_usage>5:

            st.write("Your phone usage is high. "
                 "Try reducing unnecessary screen time and keeping your phone away during study sessions.")
            st.link_button("Learn About Digital Detox",
        "https://www.nhs.uk/every-mind-matters/mental-health-issues/how-to-manage-your-screen-time/")
        if sleep_hours < 6:

            st.write(
                "Your sleep hours are low. "
                "Try maintaining a regular sleep routine and getting enough rest."
            )
            st.link_button(
                "Learn About Healthy Sleep",
                "https://www.cdc.gov/sleep/about/index.html"
            )
        if exercise < 30:


            st.write(
                "Your exercise time is low. "
                "Try adding some regular physical activity to your daily routine."
            )

            st.link_button(
                "Learn About Physical Activity",
                "https://www.who.int/news-room/fact-sheets/detail/physical-activity"
            )
        if stress >= 7:

            st.write(
                "Your stress level is high. "
                "Try a short breathing and relaxation exercise."
            )

            st.link_button(
                "Learn Breathing Exercises",
                "https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/breathing-exercises-for-stress/"
            )
        if focus < 5:

            st.write(
                "Your focus score is low. "
                "Try a distraction-free study session and keep your phone away while studying."
            )

            st.link_button(
                "Learn Focus Techniques",
                "https://todoist.com/productivity-methods/pomodoro-technique"
            )
main()



