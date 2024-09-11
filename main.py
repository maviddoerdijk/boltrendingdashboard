import streamlit as st
import pandas as pd
from load_data import load_data

# Laad de data
data = load_data()

# Titel van de app
st.title("Bol trends & innovatiemogelijkheden")

# Inleiding of algemene beschrijving van het dashboard
st.markdown("""
Welkom bij het Bol.com trends en innovatiemogelijkheden dashboard. Dit dashboard biedt inzicht in zoektrends, productmarges, 
leveringstijden en meer. Gebruik de tabs hieronder om door de verschillende secties te navigeren.
""")

# Tabs voor verschillende secties van het dashboard
tab1, tab2, tab3 = st.tabs(["Productanalyse: Innovatiemogelijkheden", "Zoektrends", "Bol.com Nieuws"])

with tab1:    
    # Gebruik van kolommen om charts naast elkaar te plaatsen
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Producten met grootste marges - Alibaba vs bol.com prijzen")
        st.bar_chart(data['product_margins'].set_index('product'))

    with col2:
        st.subheader("Top omzet producten zonder voorraad sinds afgelopen week")
        st.bar_chart(data['top_products_no_stock'].set_index('product'))
        
with tab2:
    st.header("Zoektrends")

    st.subheader("Seizoensgebonden zoekvolume")
    st.line_chart(data['seasonal_search_volume'].set_index('month'))


with tab3:
    st.header("Bol.com Nieuws")
    
    # Laatste Bol.com nieuws in een enkele sectie
    st.subheader("Bol Updates")
    st.markdown("""
    **Bol verhoogt na twee jaar weer de prijs van Select - Twinkle Magazine** - Leestijd: 3 minuten

    Select-leden van bol moeten vanaf 8 oktober 3 euro meer betalen voor het jaarabonnement. 
    De Twinkle100-aanvoerder verhoogt de prijs van Select van 11.99 naar 14.99 euro.
    """)

# Footer sectie met eventueel extra uitleg of bronnen
st.markdown("""
---
Dit dashboard is ontwikkeld om inzichten te bieden in de huidige trends en innovatiekansen voor Bol.com. 
De data is fictief en dient enkel als voorbeeld.
Voor een uitgebreide persoonlijke analyse, neem contact op met David - [MarketMaster: Actionable Insights](https://www.linkedin.com/in/david-moerdijk-754049202/).
""")
