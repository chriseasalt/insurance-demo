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

import time

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code


st.set_page_config(page_title="Purchase Here", page_icon="☎️")
st.markdown("# Purchase Here")
st.sidebar.header("Purchase Here")
st.write(
    """### Ready to purchase your insurance premium? Leave your contacts here below for us to get back to you."""
)

container_1 = st.container()
container_1.empty() 


with container_1:
    with st.form('input_form'):
        query = st.text_area("Fill in your details below and we'll reach out to you")
        submitted_input = st.form_submit_button('Submit Enquiry')
        print(query) # works fine

    if submitted_input:
        with st.spinner(text='This may take a moment...'):
            st.text("Your submission has been received. We will get back to you in 2 working days") # simulated response