# Base Url
from finviz.screener import Screener
from urllib3.exceptions import InsecureRequestWarning
from ticker import Ticker

class Screeners:
    # Names of screeners
    insider_buy = "insider_buy"
    squeeze = "squeeze"
    top_gainer = "top_gainer"
    ma50_cross = "ma50_cross"
    sleeping_monster = "sleeping_monster"
    unusual_volume = "unusual_volume"
    
    all = [insider_buy, squeeze, top_gainer, ma50_cross, sleeping_monster, unusual_volume]


class StockAPI:
    # Screener options
    screener_options = {
        # "insider_buy": [f["s"]["it_latestbuys"], f["f"]["cap_smallover,sh_avgvol_o750,sh_relvol_o1"], f["ft"]["4"]],
        "insider_buy": {
            "signal": "it_latestbuys",
            "filters": ["cap_smallover", "sh_avgvol_o750", "sh_relvol_o1"],
            "order": ""
        },
        "squeeze": {
            "signal": "",
            "filters": ["sh_relvol_o2", "sh_short_o20"],
            "order": ""
        },
        "unusual_volume": {
            "signal": "ta_unusual_volumevolume",
            "filters": ["cap_smallover","ind_stocksonly","sh_avgvol_o200","sh_relvol_o5","ta_beta_o1","ta_perf_dup"],
            "order": "perfytd"
        },
        "top_gainer":{
            "signal": "ta_topgainers",
            "filters": ["cap_smallover","sh_avgvol_o500", "sh_relvol_o2"],
            "order": ""
        },
        "ma50_cross":{
            "signal": "",
            "filters": ["sh_opt_option","ta_beta_o2","ta_highlow52w_a50h","ta_sma50_pca"],
            "order": ""
        },
        "sleeping_monster": {
            "signal": "",
            "filters": ["fa_curratio_o2","fa_salesqoq_o5","sh_avgvol_o200","sh_relvol_o1","ta_highlow52w_b0to5h","ta_sma20_pa","ta_sma200_sb50","ta_sma50_sb20"],
            "order": ""
        } 
    }
    
    def get_data_from(screener_type: str):
        tickers = []
        screener = StockAPI.screener_options[screener_type]
        signal, filters, order = screener['signal'], screener['filters'], screener['order']
        stock_dict = Screener(signal=signal, filters=filters, order=order)
        # print(stock_dict.headers)
        for stock_data in stock_dict:
            ticker = Ticker(data=stock_data)
            tickers.append(ticker.name)
        return tickers


    def get_all_screeners() -> dict:
        result = []
        
        all_tickers = []
        screener_dict = {}
        # for screener in [Screeners.sleeping_monster, Screeners.ma50_cross]:
        for screener in Screeners.all:
            tickers = StockAPI.get_data_from(screener_type=screener)
            screener_dict["name"] = screener
            screener_dict["results"] = tickers
            result.append(screener_dict)
            all_tickers += tickers
            screener_dict = {}
    
        screener_dict["name"] = "Two or more"
        screener_dict["results"] = StockAPI.get_best(all_tickers)
        result.append(screener_dict)

        return result


    def get_best(stock_list):
        results = []
        best = {}
        for ticker in stock_list:
            if ticker in best:
                best[ticker] += 1
                if best[ticker] >= 1:
                    results.append(ticker)
            else:
                best[ticker] = 0
        return results


# print(StockAPI.get_all_screeners())
