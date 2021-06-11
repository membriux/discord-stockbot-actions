# Base Url
from finviz.screener import Screener

class Screeners:
    # Names of screeners
    insider_buy = "insider_buy"
    squeeze = "squeeze"
    unusual = "unusual"
    top_g = "ma50"
    sleeping = "sleeping"

class StockAPI:
    screener_url = "https://finviz.com/screener.ashx?"
    
    # Screener options
    screener_options = {
        # "insider_buy": [f["s"]["it_latestbuys"], f["f"]["cap_smallover,sh_avgvol_o750,sh_relvol_o1"], f["ft"]["4"]],
        "insider_buy": {
            "signal": "it_latestbuys",
            "filters": ["cap_smallover", "sh_avgvol_o750", "sh_relvol_o1"]
        },
        "squeeze": "v=111&f=sh_relvol_o2,sh_short_o20",
        "unusual": "v=111&s=ta_unusualvolume&f=cap_smallover,ind_stocksonly,sh_avgvol_o200,sh_relvol_o5,ta_beta_o1,ta_perf_dup&ft=4&o=perfytd",
        "top_g": "v=111&s=ta_topgainers&f=cap_smallover,sh_avgvol_o500,sh_relvol_o2",
        "ma50": "v=111&f=sh_opt_option,ta_beta_o2,ta_highlow52w_a50h,ta_sma50_pca&ft=4",
        "sleeping": "v=111&f=fa_curratio_o2,fa_salesqoq_o5,sh_avgvol_o200,sh_relvol_o1,ta_highlow52w_b0to5h,ta_sma20_pa,ta_sma200_sb50,ta_sma50_sb20&ft=4"
    }
    
    def get_data_from(screener_type):
        f = StockAPI.screener_options[screener_type]
        print(f)
        stock_list = Screener(signal=f['signal'], filters=f['filters'])
        return stock_list



print(StockAPI.get_data_from(Screeners.insider_buy))



