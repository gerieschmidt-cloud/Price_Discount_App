
import streamlit as st

# Title
st.title("Sales Price and Discount Analysis")

# Input fields
plp = st.number_input('Previous List Price ($)', min_value=0.0, format="%0.2f")
clp = st.number_input('Current List Price ($)', min_value=0.0, format="%0.2f")
pdisc = st.number_input('Previous Discount (%)', min_value=0.0, format="%0.2f")
cdisc = st.number_input('Current Discount (%)', min_value=0.0, format="%0.2f")

# Perform calculations only if all inputs are provided
if plp > 0 and clp > 0 and pdisc >= 0 and cdisc >= 0:
    pspcalc = round(plp * (1 - (pdisc / 100)), 2)
    cspcalc = round(clp * (1 - (cdisc / 100)), 2)
    lpdeltacalc = round((clp - plp) / plp * 100, 2)
    dpdeltapptcalc = round(cdisc - pdisc, 2)
    dpdeltapctcalc = round((cdisc - pdisc) / pdisc * 100, 2) if pdisc != 0 else 0
    spdeltacalc = round((cspcalc - pspcalc) / pspcalc * 100, 2)
    prlpdeltacalc = round((1 - (((clp - plp) / plp) - ((cspcalc - pspcalc) / pspcalc))) * 100, 2)

    prl100calc = round((1 - ((pspcalc * (1 + ((clp - plp) / plp * 1))) / clp)) * 100, 2)
    prl75calc = round((1 - ((pspcalc * (1 + ((clp - plp) / plp * 0.75))) / clp)) * 100, 2)
    prl50calc = round((1 - ((pspcalc * (1 + ((clp - plp) / plp * 0.50))) / clp)) * 100, 2)
    prl25calc = round((1 - ((pspcalc * (1 + ((clp - plp) / plp * 0.25))) / clp)) * 100, 2)
    prl0calc = round((1 - (pspcalc / clp)) * 100, 2)

    spexpec100 = round(pspcalc * (1 + ((clp - plp) / plp * 1)), 2)
    spexpec75 = round(pspcalc * (1 + ((clp - plp) / plp * 0.75)), 2)
    spexpec50 = round(pspcalc * (1 + ((clp - plp) / plp * 0.50)), 2)
    spexpec25 = round(pspcalc * (1 + ((clp - plp) / plp * 0.25)), 2)
    spexpec0 = round(pspcalc, 2)

    spexpecrealized = spexpec100 - pspcalc
    csprealizeddollars = round(cspcalc - pspcalc, 2)
    sprealizedpercent = round((csprealizeddollars / spexpecrealized) * 100, 2) if spexpecrealized != 0 else 0

    # Display results
    st.subheader("Discount and Sales Price Needed to Realize List Price Change")
    st.write(f"100% Realization: {prl100calc}% / ${spexpec100}")
    st.write(f"75% Realization: {prl75calc}% / ${spexpec75}")
    st.write(f"50% Realization: {prl50calc}% / ${spexpec50}")
    st.write(f"25% Realization: {prl25calc}% / ${spexpec25}")
    st.write(f"0% Realization: {prl0calc}% / ${spexpec0}")
    st.write(f"List Price Change Realized at Current Discount: {sprealizedpercent}%")
    
    st.subheader("Details")
    st.write(f"Previous Sales Price: ${pspcalc}")
    st.write(f"Current Sales Price: ${cspcalc}")
    st.write(f"Change in List Price: {lpdeltacalc}%")
    st.write(f"Change in Selling Price: {spdeltacalc}%")
    st.write(f"Change in Selling Price: ${csprealizeddollars}")
    st.write(f"Expected Price Change with List Price Change: ${spexpecrealized}")
    st.write(f"Change in Discount: {dpdeltapptcalc} ppts")
    st.write(f"Change in Discount: {dpdeltapctcalc}%")
