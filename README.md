# Finnish Architectural Landscape: A Statistical Cross Section
## In this Noetbook you can find the initial exploratory data analysis behind [this article](https://towardsdatascience.com/finnish-architectural-landscape-a-statistical-cross-section-bf68637b3eaa?sk=59ee0de17746bff5510120d421d991f5) published in [Towards Data Science](https://towardsdatascience.com/). ##

**Abstract**

In this Medium article, you can find a statistical cross-section of the Finnish architectural landscape. This article is not going to look into the architectural qualities of different offices instead it’s going to use financial data and descriptive statistics to sense the architectural market in Finland. What’s the point of using financial data? The economy as a social science is essentially concerned with how people interact with things of value. Knowing how much people are willing to pay for a particular service quite often (though not always) can give an approximate hint about the value it provides to society. Additionally, Financial information is always meticulously collected and stored for management and taxation purposes. Since every office collects and stores financial data in a similar manner, we have a common metrics to compare otherwise very different organizations. Luckily for us, this information is openly available in Finland. With the use of some basic descriptive statistics, we can now analyze the information in the field and hopefully gain some useful insights.

## [Link to Jupiter Notebook](https://github.com/Geometrein/Fin-Ark/blob/main/Finnish_Architectural_Landscape_2019.ipynb)


**The Dataset**

These are only a few of the aspects that can be studied with the underlying dataset. Those interested in their own expiration can find the dataset [here](https://github.com/Geometrein/Fin-Ark/blob/main/Database.csv). It takes time and effort to produce a datasets please follow the copyright guidelines.

**Sources**

The data for this article was provided by:
* Fonecta
* Statistics Finland

**Tools**
* **Scraping:** Beautiful Soup, Selenium
* **Analysis:** Python, Pandas, NumPy, SciPy
* **Graphs:** Matplotlib, Seaborn

**Disclaimer**

* There is a lot of “luck” involved in running an office. To an extent all listed offices are successful since we do not have information on offices that did not [survive the market](https://en.wikipedia.org/wiki/Survivorship_bias).
* Profit vs the number of employee relationships is just one feature for comparison. If you ever glanced at the financial statement of a publicly-traded company you know that one number is never enough for evaluating complex organizations.
* The article is as good as the underlying [dataset](https://github.com/Geometrein/Fin-Ark/blob/main/Database.csv). If your office is missing, it is due to Fonecta not having your office information.
* Take the results with a healthy dose of skepticism. I am neither an economist nor an an accountant.