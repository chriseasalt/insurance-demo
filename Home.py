# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="AWS Motors",
        page_icon="🚘",
    )

    st.write("# AWS Motor Company")

    st.sidebar.success("Call us today at 67387348")

    st.markdown(
        """ 
          Welcome to AWS Motor Company where we provide you a personalised insurance offer for your car.
          With 18 years of experience and advanced analytics capabilities, you can trust our advice.
        """
    )

    st.image('Car.jpeg')
          
    st.markdown(
      """ 
      ### How To Get a Quote Now
      In order to make an offer tailored to you as close as possible, we will need the following information:
      - Vehicle Brand
      - Vehicle Model
      - Vehicle Age
      - Engine Capacity Group
      - Driver Age Group
      ### Try It Out For Yourself
      """
      )

    st.markdown(
        """
        <iframe
            width="960"
            height="720"
            src="https://us-east-1.quicksight.aws.amazon.com/sn/embed/share/accounts/487201836411/dashboards/b7b60f8e-7aed-415e-a9ad-de74977abfca?directory_alias=qsdemo4daml">
        </iframe>
        """,
        unsafe_allow_html=True
    )
    


    # st.markdown(
    #     """
    #     Streamlit is an open-source app framework built specifically for
    #     Machine Learning and Data Science projects.
    #     **👈 Select a demo from the sidebar** to see some examples
    #     of what Streamlit can do!
    #     ### Want to learn more?
    #     - Check out [streamlit.io](https://streamlit.io)
    #     - Jump into our [documentation](https://docs.streamlit.io)
    #     - Ask a question in our [community
    #       forums](https://discuss.streamlit.io)
    #     ### See more complex demos
    #     - Use a neural net to [analyze the Udacity Self-driving Car Image
    #       Dataset](https://github.com/streamlit/demo-self-driving)
    #     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    # """
    # )


if __name__ == "__main__":
    run()