import streamlit as st
from backend.reporting.pptx_gen import build_pptx

st.header('Reports')
if st.button('Generate Demo Narrative'):
    st.session_state['narrative'] = (
        'ROAS improved 12% MoM driven by Search Campaign A. '
        'Spend decreased 8% on underperforming ad sets. '
        'Shift 10% budget to lookalike audiences in NSW.'
    )

if 'narrative' in st.session_state:
    st.subheader('Draft Narrative')
    st.write(st.session_state['narrative'])
    if st.button('Export PPTX'):
        path = build_pptx(st.session_state['narrative'], 'demo_report.pptx')
        st.success(f'Exported: {path}')
        with open(path, 'rb') as f:
            st.download_button('Download PPTX', data=f, file_name='ClientPulseAI_Report.pptx')
