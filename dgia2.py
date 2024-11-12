# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:38:46 2024

@author: BM27701
"""



import streamlit as st
from datetime import datetime

# Set approval threshold
APPROVAL_THRESHOLD = 18

# Title and introductory input fields
st.title("Data Governance Impact Assessment (DGIA)")

# Input fields for assessment details
assessed_name = st.text_input("Name of Assessed:")
project_name = st.text_input("Project Name:")
system_name = st.text_input("System Name:")
business_unit_name = st.text_input("Business Unit Name:")

# Section scores
total_score = 0

# Questionnaire Sections
st.subheader("1. Data Quality")
q1_1 = st.selectbox("1.1. Does the system ensure data accuracy through data validation processes?", 
                    ["Select", "Yes, comprehensive data validation checks are in place.", 
                     "Some data validation processes are in place, but limited.", 
                     "No validation processes are in place."])
if q1_1 == "Yes, comprehensive validation checks are in place.":
    total_score += 2
elif q1_1 == "Some validation processes are in place, but limited.":
    total_score += 1

q1_2 = st.selectbox("1.2. Are there mechanisms or processes to monitor and improve data quality continuously?", 
                    ["Select", "Yes, the system includes data quality monitoring processes.", 
                     "Monitoring is manual or occurs periodically.", 
                     "No monitoring mechanism exists."])
if q1_2 == "Yes, the system includes data quality monitoring processes.":
    total_score += 2
elif q1_2 == "Monitoring is manual or occurs periodically.":
    total_score += 1

st.subheader("2. Data Lineage and Metadata")
q2_1 = st.selectbox("2.1. Does the system track data lineage for key data assets?", 
                    ["Select", "Yes, lineage is fully traceable from source to output for data assets.", 
                     "Partially, lineage is captured for some key data assets.", 
                     "No lineage tracking is in place."])
if q2_1 == "Yes, lineage is fully traceable from source to output.":
    total_score += 2
elif q2_1 == "Partially, lineage is captured for some key data assets.":
    total_score += 1

q2_2 = st.selectbox("2.2. Is metadata in scope to be captured and managed within the system?", 
                    ["Select", "Yes, a metadata management process is in scope to be managed.", 
                     "Metadata is to be ingested but is not in scope.", 
                     "No metadata management process exists."])
if q2_2 == "Yes, a metadata management process is in scope to be managed.":
    total_score += 2
elif q2_2 == "Metadata is to be ingested but is not in scope.":
    total_score += 1

st.subheader("3. Data Classification and Security")
q3_1 = st.selectbox("3.1. Are data classification levels defined and adhered to?", 
                    ["Select", "Yes, data is classified according to policy, with defined levels.", 
                     "Partial classification is in place, covering some critical data types.", 
                     "No data classification is implemented."])
if q3_1 == "Yes, data is classified according to policy, with defined levels.":
    total_score += 2
elif q3_1 == "Partial classification is in place, covering some data types.":
    total_score += 1

q3_2 = st.selectbox("3.2. Are access controls and permissions aligned with data sensitivity?", 
                    ["Select", "Yes, access controls strictly follow data classification.", 
                     "Access controls are implemented but not strictly followed.", 
                     "No access control mechanism is in place."])
if q3_2 == "Yes, access controls strictly follow data classification.":
    total_score += 2
elif q3_2 == "Access controls are implemented but not strictly followed.":
    total_score += 1

q3_3 = st.selectbox("3.3. Does the system use encryption for sensitive data both in transit and at rest?", 
                    ["Select", "Yes, encryption is used for both in transit and at rest.", 
                     "Partial encryption is in place.", 
                     "No encryption mechanisms exist."])
if q3_3 == "Yes, encryption is used for both in transit and at rest.":
    total_score += 2
elif q3_3 == "Partial encryption is in place.":
    total_score += 1

st.subheader("4. Compliance and Regulatory Alignment")
q4_1 = st.selectbox("4.1. Are data retention and disposal policies applied consistently within the system?", 
                    ["Select", "Yes, data retention and disposal are aligned with policy.", 
                     "Some retention policies are applied, but not comprehensively.", 
                     "No retention or disposal policies are implemented."])
if q4_1 == "Yes, data retention and disposal are aligned with policy.":
    total_score += 2
elif q4_1 == "Some retention policies are applied, but not comprehensively.":
    total_score += 1

q4_2 = st.selectbox("4.2. Is there an audit trail for data access and modifications?", 
                    ["Select", "Yes, a complete audit trail is available.", 
                     "Partial audit logging is implemented.", 
                     "No audit logging is implemented."])
if q4_2 == "Yes, a complete audit trail is available.":
    total_score += 2
elif q4_2 == "Partial audit logging is implemented.":
    total_score += 1

st.subheader("5. Data Risk and Mitigation")
q5_1 = st.selectbox("5.1. Have data governance risks been identified and documented?", 
                    ["Select", "Yes, a full risk assessment has been conducted.", 
                     "Data risks are identified informally or in part.", 
                     "No risk assessment has been done."])
if q5_1 == "Yes, a full risk assessment has been conducted.":
    total_score += 2
elif q5_1 == "Risks are identified informally or in part.":
    total_score += 1

q5_2 = st.selectbox("5.2. Are mitigation measures implemented for all identified risks?", 
                    ["Select", "Yes, all identified risks have mitigation plans.", 
                     "Some risks have mitigation plans.", 
                     "No mitigation plans are in place."])
if q5_2 == "Yes, all identified risks have mitigation plans.":
    total_score += 2
elif q5_2 == "Some risks have mitigation plans.":
    total_score += 1

st.subheader("6. Data Governance Monitoring and Review")
q6_1 = st.selectbox("6.1. Will ongoing data governance monitoring be conducted for this system?", 
                    ["Select", "Yes, there is a scheduled process for ongoing monitoring.", 
                     "Monitoring will occur occasionally or on-demand.", 
                     "No ongoing monitoring process is defined."])
if q6_1 == "Yes, there is a scheduled process for ongoing monitoring.":
    total_score += 2
elif q6_1 == "Monitoring occurs occasionally or on-demand.":
    total_score += 1

q6_2 = st.selectbox("6.2. Is there a formal process for periodic data control review and updates to the system?", 
                    ["Select", "Yes, periodic data control reviews and updates are planned.", 
                     "Data control reviews will be conducted informally or infrequently.", 
                     "No review or update process is defined."])
if q6_2 == "Yes, periodic data control reviews and updates are planned.":
    total_score += 2
elif q6_2 == "Data control reviews will be conducted informally or infrequently.":
    total_score += 1

st.subheader("7. Critical Data Elements (CDEs)")
q7_1 = st.selectbox("7.1. Has a formal process been used to identify Critical Data Elements (CDEs) for this system?", 
                    ["Select", "Yes, a defined process identifies all CDEs based on risk, value, or regulatory impact.", 
                     "Some CDEs are identified, but without a formal process.", 
                     "No formal identification of CDEs has been performed."])
if q7_1 == "Yes, a defined process identifies all CDEs based on risk, value, or regulatory impact.":
    total_score += 2
elif q7_1 == "Some CDEs are identified, but without a formal process.":
    total_score += 1

# Approval Decision
if st.button("Submit Assessment"):
    # Capture the date of the assessment
    assessment_date = datetime.now().strftime("%Y-%m-%d")

    if total_score >= APPROVAL_THRESHOLD:
        st.success("Approved: Your system meets the Data Governance Impact Assessment criteria. Please proceed as required")
    else:
        st.error("Unapproved: Your system does not meet the Data Governance Impact Assessment criteria. Please review and address the identified areas.")

    # Display assessment details
    st.write("### Assessment Details")
    st.write(f"**Name of Assessed**: {assessed_name}")
    st.write(f"**Project Name**: {project_name}")
    st.write(f"**System Name**: {system_name}")
    st.write(f"**Business Unit Name**: {business_unit_name}")
    st.write(f"**Assessment Date**: {assessment_date}")
    st.write(f"**Total Score**: {total_score}")
