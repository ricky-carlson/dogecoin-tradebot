# dogecoin-tradebot

This program is anticipated to succesfully trade Dogecoin over a medium-to-long-term time horizon. Success will be measured by the trading bot's ability to generate returns in excess of brokerage and other related fees. 

General Framework:

Trading bot will take several inputs to determine whether or not a trade should be taken or discarded
  - Sentiment of Dogecoin measured by conversational/mentioned activity on social media sites like Twitter, Facebook, and through Google Searches

  - Dogecoin price activity measured by relative price performance 
    * Price change after 5m, 15m, 30m, etc

  - !Sentiment_Score! will be created using both inputs described above, the higher the score the more viable a trade.
    * Ex: Elevated social media activity paired with strong relative price performance would garner a high !Sentiment_Score!
    * Ex: Reversal trade - Low !Sentiment_Score! could be followed by high !Sentiment_Score! and vice versa.
    * Buy while !Sentiment_Score! is low and sell when !Sentiment_Score! is high

  - Trade levels determined using price performance data to establish upper and lower levels
    * Upper and lower levels established using 1 or 2 standard deviations above and below relative average price
    - When price performance is stronger, average price should be calculated using more recent price data
    - When price performance is weaker, average price should be calculated using less recent price data
