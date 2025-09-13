# FortuneTeller
Based off of the 2025 MITSUI&amp;CO challenge, this project aims to predict the commodity returns of foreign exchange futures.

My goals, aside from the most obvious one, are to:

1️⃣ Be able to use more regression-based models hand-in-hand with ensuring statistical significance

2️⃣ Have clearer and more concise code

3️⃣Measure accuracy with various metrics

4️⃣Have a fully presentable product with visualization that is applicable in any field for futures commodity return predictions

9/13/2025: I have created and implemented a decision stump to determine whether or not the future's prices are in contango or not, which is relevant todetermine the roll return, an essential part of calculating total commodity return; the reason I did not extend this further into a multi-class analysis tool, including backwardation, is because I thought it would be much more pertinent to trade off of one indicator for the time being. However, I want to determine whether or not including multiple classes would yield a more effective outcome by utilizing my protoype trading engine in StockBot and backtesting with metrics besides the Sharpe ratio, such as the Sortino and Calmar ratios, as well as maximum drawdown. For now, my current approach revolves around linear regression with varying degrees of fitting along with the tree split to evaluate contango, in which I used a custom statistical criterion (logarithms of p-values for all possibble outcomes). As I continue to develop this project, my methodology remains the same as before: I want to manually develop and encode logarithmic regression as well as tree-based modeling that echoes XGBoost to be able to more accurately predict future prices. This would allow me to more accurately predict commodity returns and, additionally, to predict buy/sell limits on contracts. Eventually, my hope is to be able to integrate this with the StockBot trading engine and backtester.
