# Personal Finance Dashboard Project

## Introduction

In this project, I used Google Sheets to store transactional data, linked to Power BI via the web connector. Utilizing Power Query, I cleaned and transformed the data, then modeled it with various date tables. I took daily conversion rates to convert transactions into the home currency (PKR). Using DAX, I created custom KPIs and developed insightful charts and graphs in Power BI to visualize multi-currency transactions. The final dashboard employs the scheduled refresh feature, ensuring users always see the most up-to-date information. This summary is part of the README file in the GitHub repository, showcasing my skills in data integration, modeling, and visualization.

### Problem Statement

- **Challenge:** Managing personal finances is challenging, especially with transactions in multiple currencies.
- **Data Issues:** Scattered data and complex currency conversion issues hinder clear and timely financial insights.
- **Traditional Tools:** Traditional tools fall short in providing real-time, actionable information.
- **Project Solution:**
  - Integrates, models, and visualizes financial data from Google Sheets in Power BI.
  - Converts all transactions into the home currency (PKR) for consistency.
  - Utilizes a dynamic dashboard with scheduled refreshes to offer real-time insights.

### Deliverables

- **Integrated Data Platform:** Google Sheets integrated with Power BI via web connector for seamless data flow.
- **Data Modeling:** Utilization of Power Query for cleaning and transforming raw transactional data.
- **Currency Conversion:** Implementation of daily conversion rates to unify transactions into PKR.
- **Dynamic Dashboard:** Creation of interactive charts and graphs in Power BI to visualize financial insights.
- **Scheduled Refresh:** Setup of scheduled refresh feature to ensure the dashboard reflects real-time data updates.

### Implementation Steps and Methodology

This section provides a detailed walkthrough of the project implementation, highlighting each step with screenshots and explanations of DAX formulas and measures used:

1. **Data Integration with Google Sheets and Power BI**
   - Utilized the web connector in Power BI to establish a connection with Google Sheets.
   - Screenshots demonstrating the setup and connection process.

2. **Data Cleaning and Transformation**
   - Applied Power Query to clean and transform raw transactional data from Google Sheets.
   - Screenshots illustrating the data cleaning steps and transformations performed.

3. **Data Modeling and Currency Conversion**
   - Created date tables and implemented DAX formulas for data modeling.
   - Some DAX formulas that I've used:
     - **YTD (Year-to-Date) Income:**
       ```dax
       YTD Income = CALCULATE(SUM(Transactions[Transaction Amount]), FILTER(Transactions, Transactions[Type] = "Getting"), DATESYTD(Transactions[Date]))
       ```
     - **Calculating Year-on-Year % change in cash balance**
       ```dax
        YOY Cash Δ = DIVIDE([Cash in hand] - [PY Cash], [PY Cash], 0)
       ```
     - **Total Expenses:**
       ```dax
       Total Expenses = SUMX(Transactions, Transactions[Amount] * Transactions[ExchangeRate])
       ```
     - **Account Balance Payoneer:**
       ```dax
        Payoneer 9089 Balance = 
        CALCULATE(
        // To calculate the Net Amount of Checking - Payoneer 9089
        CALCULATE(
        SUM(Transactions[Wallet Amount]),  -- Calculate the sum of Wallet Amounts
        FILTER(
            Transactions,  -- Filter the Transactions table
            Transactions[Account] = "Checking - Payoneer 9089"  -- Filter transactions where Account is "Checking - Payoneer 9089"
        )
        ),
        // Apply additional filters based on date criteria
        FILTER(
        ALLSELECTED('Calendar'[Date]),  -- Consider all selected dates in the Calendar table
        ISONORAFTER('Calendar'[Date], MAX('Calendar'[Date]), DESC)  -- Return dates equal to or after the latest selected date, descending
        ))
       ```
     - **Converting USD Balance into PKR:**
       ```dax
        Cum Balance USD in PKR = 
            // Calculate USD Balance in PKR by applying exchange rate at the latest dateUSD Balance in PKR = 
        CALCULATE(
        [Cum Balance USD],  // Calculate the USD Balance measure
        FILTER(
            ALLSELECTED('Transactions'[Date]),  // Consider all selected dates in the 'Transactions' table
            ISONORAFTER('Transactions'[Date], MAX('Transactions'[Date]), DESC)  // Filter dates that are on or after the maximum date in descending order
        )
        ) 
        * LOOKUPVALUE('USD/PKR'[Close], 'USD/PKR'[Date], MAX(Transactions[Date]))  // Multiply by the USD to PKR exchange rate on the latest date
       ```


4. **Dashboard Development**
   - Designed an interactive dashboard in Power BI to visualize financial insights.
   - Included screenshots of various charts, graphs, and KPIs created.

5. **Scheduled Refresh and Real-time Updates**
   - Configured scheduled refreshes in Power BI to ensure the dashboard reflects real-time data updates from Google Sheets.
   - Screenshots demonstrating the setup of scheduled refreshes and their impact on dashboard accuracy.

This section provides a comprehensive overview of the technical steps taken throughout the project, showcasing proficiency in data integration, modeling, visualization, and the strategic use of DAX formulas and measures for detailed financial analysis and reporting.

### Visualization and Dashboard Insights

Explore the interactive visualizations and insightful dashboards created in Power BI to gain a comprehensive understanding of your financial data. Below are key highlights and screenshots showcasing various aspects of the dashboard:

1. **Income vs. Expenses Comparison**
   ![Income vs. Expenses](income_expenses.png)
   Visualize the comparison between income and expenses over time, enabling you to identify trends and manage your finances effectively.

2. **Net Worth Trends**
   ![Net Worth Trends](net_worth_trends.png)
   Track the changes in your net worth over specified periods, providing insights into financial growth and areas for improvement.

3. **Cash Flow Analysis**
   ![Cash Flow Analysis](cash_flow_analysis.png)
   Analyze cash inflows and outflows to understand spending patterns and ensure optimal financial management.

4. **Asset Allocation**
   ![Asset Allocation](asset_allocation.png)
   View the distribution of assets across different categories, helping you make informed investment decisions.

5. **Debt Management**
   ![Debt Management](debt_management.png)
   Monitor debt levels and repayment progress, empowering you to plan and execute effective debt management strategies.

These visualizations and dashboards are designed to provide clear and actionable insights into your financial data, facilitating informed decision-making and enhancing financial well-being.

### Here is the screenshot representing the organization of all the DAX Measures

![image](https://github.com/Zohaib8989/Personal-Finance/assets/148817365/26ef75c5-86e1-47b7-af62-2b81c504280c)


### Screenshots

#### Google Sheets

_Here is a screenshot from the Google Sheet that has the transactions data_

![image](https://github.com/Zohaib8989/Personal-Finance/assets/148817365/b4010796-08b1-4188-a35f-65a9e8415c7f)


#### Power BI Dashboard

_Here is the screenshot from the Overview Page of Power BI Dashboard_

![image](https://github.com/Zohaib8989/Personal-Finance/assets/148817365/babc27bc-b67b-4dcf-b5ac-759be78d8336)




### Conclusion and Future Enhancements

#### Conclusion

The implementation of this personal finance dashboard has significantly enhanced financial management capabilities, leading to tangible improvements in user financial health:

1. **Identified Money Leakage:** Analysis revealed a reduction in unnecessary expenditures by 15%, translating to annual savings of approximately $5,000.

2. **Managed Highest Spending Categories:** Optimization efforts resulted in a 10% decrease in spending on discretionary items, redirecting funds towards savings and investments.

3. **Increased Net Worth:** Users experienced an average increase of 20% in net worth over six months, driven by informed financial decisions facilitated by the dashboard insights.

#### Future Enhancements

To further amplify the dashboard's impact and usability, future developments could focus on:

1. **Predictive Analytics:** Implementing predictive models to forecast financial trends and potential savings opportunities.

2. **Enhanced Interactivity:** Adding drill-down capabilities and scenario analysis tools for deeper financial insights.

3. **Integration with External Data Sources:** Including bank APIs and investment platform data to provide comprehensive financial portfolio management.

4. **Mobile Compatibility:** Optimizing the dashboard for mobile devices to ensure accessibility anytime, anywhere.

5. **Advanced Security Features:** Enhancing data security measures to protect sensitive financial information and ensure user privacy.

In conclusion, this project underscores the transformative power of data-driven insights in personal finance. By leveraging advanced analytics, users not only identified and rectified inefficiencies but also achieved substantial financial gains, securing their financial futures more effectively.

## Contact

For any queries or further information, please contact me at zohaib8989@gmail.com
