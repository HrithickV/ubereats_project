import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="UberEats Bangalore Dashboard", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Project Introduction", "Restaurant Analysis (10 Qs)", "Order Analysis (5 Qs)"])

# --- PAGE 1: INTRODUCTION ---
if page == "Project Introduction":
    st.title("🍴 UberEats Bangalore Data Analysis")
    st.markdown("""
    ### Project Overview
    This project analyzes the food delivery ecosystem in Bangalore. 
    By exploring restaurant data and ordering patterns, we aim to uncover insights 
    into pricing, ratings, and popular cuisines.
    """)
    st.info("Select a category in the sidebar to view specific analysis results.")

# --- PAGE 2: RESTAURANT ANALYSIS ---
elif page == "Restaurant Analysis (10 Qs)":
    st.title("📊 Restaurant Insights")
    
    # List of all 10 questions
    q_list = [
        "1. Highest Average Restaurant Ratings by Location",
        "2. Over-saturated Locations",
        "3. Impact of Online Ordering on Ratings",
        "4. Table Booking vs Customer Ratings",
        "5. Price Range vs Customer Satisfaction",
        "6. Performance by Cost Segments (Min/Max Analysis)",
        "7. Most Common Cuisines in Bangalore",
        "8. Highest Rated Cuisines",
        "9. Hidden Gems (Low count, High rating)",
        "10. Relationship between Cost and Rating"
    ]
    selected_q = st.selectbox("Select an Analysis Question", q_list)

    # All logic below is indented correctly inside the "Restaurant Analysis" page
    if selected_q == q_list[0]:
        st.subheader("📍 Highest Average Restaurant Ratings by Location")
        data1 = {
            'Locations': ['Lavelle Road', 'Koramangala 5th Block', 'St. Marks Road', 'Sankey Road', 'Koramangala 3rd Block', 'Cunningham Road', 'Sadashiv Nagar', 'Residency Road', 'Koramangala 2nd Block', 'Ulsoor'],
            'Avg Rating': [0.77, 0.76, 0.74, 0.74, 0.74, 0.74, 0.73, 0.73, 0.73, 0.72]
        }
        df1 = pd.DataFrame(data1)
        fig1 = px.bar(df1, x='Avg Rating', y='Locations', orientation='h', color='Avg Rating', color_continuous_scale='Viridis')
        fig1.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig1, use_container_width=True)
        st.write("### 📋 Data Table")
        st.table(df1) # Static table, not editable

    elif selected_q == q_list[1]:
        st.subheader("🏙️ Over-saturated Locations")
        data2 = {
            'Location': ['Koramangala 5th Block', 'BTM', 'Indiranagar', 'HSR', 'Jayanagar', 'JP Nagar', 'Whitefield', 'Koramangala 7th Block', 'Koramangala 6th Block', 'Marathahalli'],
            'Restaurant_count': [1782, 1454, 1346, 1161, 1037, 1016, 824, 723, 718, 680]
        }
        df2 = pd.DataFrame(data2)
        fig2 = px.bar(df2, x='Restaurant_count', y='Location', orientation='h', color='Restaurant_count', color_continuous_scale='Reds')
        fig2.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig2, use_container_width=True)
        st.write("### 📋 Data Table")
        st.table(df2)

    elif selected_q == q_list[2]:
        st.subheader("📱 Does online ordering improve restaurant ratings?")
        data3 = {
            'Online Order': ['No', 'Yes'],
            'Avg Rating': [3.93, 3.89],
            'Total Restaurants': [6823, 16335]
        }
        df3 = pd.DataFrame(data3)
        st.plotly_chart(px.bar(df3, x='Online Order', y='Avg Rating', color='Online Order'), use_container_width=True)
        st.table(df3)

    elif selected_q == q_list[3]:
        st.subheader("📅 Table Booking vs Customer Ratings")
        data4 = {
            'Table Booking': ['No', 'Yes'],
            'Avg Rating (0-5)': [3.81, 4.16],
            'Total Count': [17057, 6101]
        }
        df4 = pd.DataFrame(data4)
        st.plotly_chart(px.pie(df4, names='Table Booking', values='Total Count'), use_container_width=True)
        st.table(df4)

    elif selected_q == q_list[4]:
        st.subheader("💰 Price Range vs Customer Satisfaction")
        # Data from your Q5 SQL result
        data5 = {
            'Cost_segment': ['Premium', 'Budget', 'Mid-range'],
            'Avg rating(satisfaction)': [4.12, 3.82, 3.81],
            'Total restaurants': [6668, 6785, 9705]
        }
        df5 = pd.DataFrame(data5)
        st.plotly_chart(px.bar(df5, x='Cost_segment', y='Avg rating(satisfaction)', color='Cost_segment'), use_container_width=True)
        st.table(df5)

    elif selected_q == q_list[5]:
        st.subheader("📊 Performance by Cost Segments (Full Analysis)")
        # Data from your Q6 SQL result
        data6 = {
            'Cost_segment': ['Premium', 'Budget', 'Mid-range'],
            'Avg_rating': [4.12, 3.82, 3.81],
            'Min_rating': [1.8, 2.1, 2.0],
            'Max_rating': [4.9, 4.9, 4.7],
            'Total_restaurants': [6668, 6785, 9705]
        }
        df6 = pd.DataFrame(data6)
        st.plotly_chart(px.bar(df6, x='Cost_segment', y=['Min_rating', 'Avg_rating', 'Max_rating'], barmode='group'), use_container_width=True)
        st.table(df6)

    elif selected_q == q_list[6]:
        st.subheader("🍜 Most Common Cuisines in Bangalore")
        data7 = {
            'cuisine type': ['North Indian', 'North Indian, Chinese', 'South Indian', 'Cafe', 'South Indian, North Indian, Chinese', 'Bakery, Desserts', 'Desserts, Beverages', 'Chinese', 'Ice Cream, Desserts', 'Desserts'],
            'No_of_restaurants': [1144, 776, 359, 273, 233, 215, 214, 210, 208, 206]
        }
        df7 = pd.DataFrame(data7)
        st.plotly_chart(px.pie(df7, values='No_of_restaurants', names='cuisine type'), use_container_width=True)
        st.table(df7)

    elif selected_q == q_list[7]:
        st.subheader("⭐ Highest Rated Cuisines")
        data8 = {
            'Cuisines': ['North Indian, Thai, Japanese, Continental, Cafe', 'Cafe, American, Burger, Steak', 'North Indian, European, Mediterranean, BBQ, Kebab', 'Ice Cream, Cafe, Pizza, Burger, Desserts, Beverages', 'Pizza, Cafe, Italian'],
            'Avg_rating': [4.69, 4.6, 4.53, 4.42, 4.41],
            'Total_restaurants': [34, 43, 39, 33, 85]
        }
        df8 = pd.DataFrame(data8)
        st.plotly_chart(px.bar(df8, x='Avg_rating', y='Cuisines', orientation='h'), use_container_width=True)
        st.table(df8)

    elif selected_q == q_list[8]:
        st.subheader("💎 Hidden Gems (Low count, High rating)")
        data9 = {
            'Cuisine': ['Continental, North Indian, Italian, South Indian, Finger Food', 'Asian, Chinese, Thai, Momos', 'North Indian, European, Mediterranean, BBQ', 'Asian, Mediterranean, North Indian, BBQ', 'European, Mediterranean, North Indian, BBQ'],
            'Avg_rating': [4.9, 4.9, 4.8, 4.8, 4.79],
            'Total_restaurants': [6, 19, 5, 6, 19]
        }
        df9 = pd.DataFrame(data9)
        st.plotly_chart(px.scatter(df9, x='Total_restaurants', y='Avg_rating', text='Cuisine', size='Total_restaurants'), use_container_width=True)
        st.table(df9)

    elif selected_q == q_list[9]:
        st.subheader("💸 Relationship between Cost and Rating")
        data10 = {
            'Price_range': ['luxury (2000+)', 'premium (1001 - 2000)', 'mid-range (501-1000)', 'budget (0-500)'],
            'Avg_rating': [4.2, 4.17, 3.89, 3.79],
            'Count': [537, 4203, 8643, 9775]
        }
        df10 = pd.DataFrame(data10)
        st.plotly_chart(px.line(df10, x='Price_range', y='Avg_rating', markers=True), use_container_width=True)
        st.table(df10)

# --- PAGE 3: ORDER ANALYSIS ---
# --- PAGE 3: ORDER ANALYSIS ---
elif page == "Order Analysis (5 Qs)":
    st.title("📦 Order Pattern Analysis")
    
    order_q_list = [
        "1. Most popular day of the week for ordering",
        "2. Top 5 restaurants by revenue",
        "3. Impact of discounts on spending",
        "4. Payment methods for expensive orders",
        "5. Salary Day Effect (Spending at start of month)"
    ]
    selected_order_q = st.selectbox("Select an Order Question", order_q_list)

    # 1. Popular Day of Week
    if selected_order_q == order_q_list[0]:
        st.subheader("🗓️ Orders by Day of the Week")
        data = {
            'Day_of_week': ['thursday', 'monday', 'wednesday', 'tuesday', 'friday', 'saturday', 'sunday'],
            'order_count': [3623, 3613, 3598, 3596, 3567, 3505, 3498]
        }
        df = pd.DataFrame(data)
        st.plotly_chart(px.bar(df, x='Day_of_week', y='order_count', color='order_count', color_continuous_scale='Blues'), use_container_width=True)
        st.write("### 📋 Editable Data Table")
        st.data_editor(df, use_container_width=True, hide_index=True)

    # 2. Top 5 Restaurants by Revenue
    elif selected_order_q == order_q_list[1]:
        st.subheader("💰 Top 5 Revenue-Generating Restaurants")
        data = {
            'Restaurant Name': ["Bob's Bar", "Cake Cafe", "Biryani Mane", "Hungry Lee", "Andhra Grills"],
            'Total Revenue (₹)': [19518.1, 19335.2, 19249.5, 19167.5, 19153.7],
            'Order Count': [15, 19, 15, 18, 19]
        }
        df = pd.DataFrame(data)
        st.plotly_chart(px.bar(df, x='Total Revenue (₹)', y='Restaurant Name', orientation='h', color='Total Revenue (₹)'), use_container_width=True)
        st.data_editor(df, use_container_width=True, hide_index=True)

    # 3. Discount vs Spending
    elif selected_order_q == order_q_list[2]:
        st.subheader("🎟️ Does using a discount result in higher spending?")
        data = {
            'Discount Used?': ['Yes', 'No'],
            'Avg Order Value (₹)': [1149.91, 822.49],
            'Order Count': [12491, 12509]
        }
        df = pd.DataFrame(data)
        st.plotly_chart(px.bar(df, x='Discount Used?', y='Avg Order Value (₹)', color='Discount Used?'), use_container_width=True)
        st.data_editor(df, use_container_width=True, hide_index=True)

    # 4. Payment Method for Expensive Orders
    elif selected_order_q == order_q_list[3]:
        st.subheader("💳 Payment Methods for High-Value Orders")
        data = {
            'Payment Method': ['Card', 'UPI', 'Cash'],
            'Avg Order Value (₹)': [989.02, 985.75, 983.47],
            'Order Count': [8364, 8252, 8384]
        }
        df = pd.DataFrame(data)
        st.plotly_chart(px.bar(df, x='Payment Method', y='Avg Order Value (₹)', color='Avg Order Value (₹)'), use_container_width=True)
        st.data_editor(df, use_container_width=True, hide_index=True)

    # 5. Salary Day Effect
    elif selected_order_q == order_q_list[4]:
        st.subheader("📈 Salary Day Effect (Month Start Spending)")
        data = {
            'Day of Month': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '30', '31'],
            'Avg Spend (₹)': [995.09, 977.93, 1001.01, 1007.50, 986.58, 997.16, 995.73, 972.33, 987.60, 1000.67, 997.73, 1010.84],
            'Order Count': [852, 848, 815, 857, 832, 863, 781, 811, 814, 865, 821, 507]
        }
        df = pd.DataFrame(data)
        st.plotly_chart(px.line(df, x='Day of Month', y='Avg Spend (₹)', markers=True), use_container_width=True)
        st.data_editor(df, use_container_width=True, hide_index=True)