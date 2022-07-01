import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":ocean:", layout="wide")
st.markdown(
        """
        <style>
@font-face {
  font-family: 'Lora';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.googleapis.com/css2?family=Lato&family=Lora:wght@500&display=swap) format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

    html, body, [class*="css"]  {
    font-family: 'Lora';
    }
    </style>

    """,
        unsafe_allow_html=True,
    )

st.markdown("""
			<style>
				.main-font {
    			font-size:25px !important;
    			font-weight: bold;
				}
			</style>
		""", unsafe_allow_html=True)


# ---- HEADER SECTION ----
with st.container():
	st.subheader("Hi, I'm Sophia :musical_note:")
	st.title("Welcome to my homepage!")
	#st.markdown('<p class="main-font">Hi, I'm Sophia :musical_note:</p>', unsafe_allow_html=True)
	#st.markdown('<p class="main-font">Welcome to my homepage!</p>', unsafe_allow_html=True)
	#st.title("Data scientist, programmer, and life-long learner")
	#st.write("I earned my undergraduate degree in Economics from Emory University, and graduated from the Georgia Institute of Technology with an MS in Analytics.")

# ---- GITHUB LINK ----	
	#st.write("[Github](https://pythonandvba.com)")

# ---- WHO I AM ----
with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.subheader("Education")
		#st.markdown('<p class="main-font">Education</p>', unsafe_allow_html=True)
		st.write("**MS in Analytics**, _Georgia Institute of Technology_")
		st.write("**BA in Economics & History**, _Emory University_")
		st.write("##")
		#st.markdown('<p class="main-font">About me</p>', unsafe_allow_html=True)
		st.subheader("About me")
		st.write(
			"""
			Software engineer and data scientist with experience in:
			- Python, having created everything from data-driven analytical tools to full-stack web applications. 
			- Java, including developing microservices using Spring Boot and graphical demos with Processing. 
			- front-end frameworks, such as React and Angular.
			- cloud technologies, specifically EC2, S3, SQS/SNS, Glue, Redshift and AWS Kinesis.

			My unique background encompasses both software development and data science, and I am interested in developing web-based applications that enable businesses to design, build, and deploy analytical models faster.
			"""

		)


		#st.markdown('<p class="main-font">Education</p>', unsafe_allow_html=True)
		#st.write("##")
		#st.write("[YouTube Channel >] ()")

