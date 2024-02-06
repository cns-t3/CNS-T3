from fastapi import FastAPI, Query, HTTPException
from typing import List
from pydantic import BaseModel
import requests


app = FastAPI()


class NewsArticle(BaseModel):
    news_id: int
    title: str
    content: str
    publisher: str
    publishedAt: str
    image_url: str
    source_url: str
    risk_rating: str
    summary: str
    score: int
    tag: str


class Person(BaseModel):
    person_id: int | None
    name: str | None
    occupation: str | None
    dob: str | None
    nationality: str | None
    description: str | None
    company: str | None
    country_of_residency: str | None
    pep_status: str | None
    source_of_wealth: str | None
    img_url: str | None


class SearchResult(BaseModel):
    person: Person
    newsArticles: List[NewsArticle]


@app.get(
    "/search",
    # response_model=SearchResult,
    tags=["search"],
    summary="Get relevant news articles and social media posts by search query",
    description="Returns person's profile and an array of news articles",
)
async def get_articles_by_query(
    search_query: str = Query(..., description="Search query of the articles to return")
):
    # get person data first
    params = {"name": search_query}
    person_endpoint = "http://127.0.0.1:8001/persons/search/"
    response = requests.get(person_endpoint, params=params)
    if response.status_code == 200:
        person = response.json()
    else:
        raise HTTPException(
            status_code=404, detail="No person found with the provided name"
        )

    news_endpoint = "http://127.0.0.1:8002/news/" + search_query
    response = requests.get(news_endpoint)
    if response.status_code == 200:
        news_articles = response.json()
        search_result = SearchResult(person=person, newsArticles=news_articles)
        return search_result

    # this is the sample data
    # profile = Profile(
    #     person_id=456,
    #     name="Tim Cook",
    #     occupation="CEO",
    #     dob="1960-11-01T00:00:00Z",
    #     nationality="American",
    #     description='Tim Cook is a distinguished business leader known for his role as the CEO of Apple Inc., a position he assumed in 2011 following the iconic Steve Jobs. Cook\'s professional trajectory is marked by his strategic vision, operational prowess, and commitment to innovation. Renowned for his disciplined management style and focus on sustainability, Cook has steered Apple through significant milestones, including the launch of groundbreaking products like the iPhone X and the Apple Watch. Under his stewardship, Apple has expanded its global footprint, diversified its product offerings, and emphasized corporate social responsibility initiatives. Cook\'s leadership is characterized by a blend of foresight, integrity, and a relentless drive for excellence, making him a pivotal figure in the tech industry.',
    #     company="Apple Inc.",
    #     img_url="https://www.apple.com/leadership/images/bio/tim-cook_image.png.og.png?1696970027442",
    # )
    # news_articles = [
    #     NewsArticle(
    #         news_id=1,
    #         title="Apple CEO Tim Cook Takes Steep Pay Cut, as Expected",
    #         content="Timothy D. Cook is, since the resignation of Steve Jobs August 24, 2011, the CEO of Apple Inc.\n\nTim Cook grew up in Alabama. His father worked in a shipyard and his mother was a housewife. Graduated in 1982 from Auburn University in Alabama in industrial engineering, he obtained his MBA in 1988 at Duke University in North Carolina, one of the most prestigious American universities.\n\nTim Cook has worked for 12 years at IBM, where he supervised the production and distribution in North America and Latin America. Then, he joined Compaq and became vice president in charge of the production, the procurement and the inventory management.\n\nSteve Jobs poached himself Tim Cook at Compaq in 1997. Tim Cook joined Apple in March 1998, a year after the return of Steve Jobs at the helm. Under the authority of Steve Jobs, Tim Cook is responsible of the supply chain managing: sales, support, customer services. He works for all markets where the company is present.\n\nTim Cook puts in place a strategy: the company must reduce its products range and the number of distributors and resellers. Another strategy initiated by Tim Cook: subcontracting in Asia. Tim Cook is the man of the relocation in the company.\n\nIn 2000, Tim Cook became director of international sales, and in 2004 he took head of the Macintosh division, which is responsible of MacBook, MacBook Pro and iMac.\n\nSince that day, Mac sales are constantly raising. Tim Cook knows how to sell. These excellent results allow him to evolve in the company. In 2007 Tim Cook became Chief Operating Officer of the company.\n\nIn 2004, when Steve Jobs was convalescing after a surgery against a pancreatic cancer, Tim Cook replaced him for two years. In 2009, Steve Jobs takes leave for a liver transplant; Tim Cook is CEO during several months. In January 2011, even if he is on the sick list, Steve Jobs is always CEO but Tim Cook is at the helm of the company daily.\n\nTim Cook is a brilliant man and very intelligent. Less impulsive than his predecessor, he can seem emotionally detached and implacable. This is a quiet man who does very few public appearances.\n\nTim Cook is on the Board of Directors of Nike, where he took lessons in marketing in contact with Phil Knight, the founder of Nike.",
    #         publisher="Market Screener",
    #         publishedAt="2024-01-11T22:30:09Z",
    #         image_url="https://www.marketscreener.com/images/twitter_MS_fdblanc.png",
    #         source_url="https://www.marketscreener.com/business-leaders/TIM-COOK-267/news/Apple-CEO-Tim-Cook-Takes-Steep-Pay-Cut-as-Expected-45727024/",
    #         risk_rating="low",
    #         summary="Timothy D. Cook, CEO of Apple Inc. since 2011, had a humble upbringing in Alabama, graduated from Auburn University and later Duke University. Cook worked at IBM and Compaq before joining Apple in 1998. Under his leadership, Apple focused on supply chain management, reducing product range, and subcontracting in Asia. Cook's strategic decisions led to increased Mac sales. He became COO in 2007 and acted as CEO during Steve Jobs' medical absences. Cook is known for his intelligence, quiet demeanor, and limited public appearances. He also serves on the Board of Directors at Nike.",
    #         score=0,
    #         tag="",
    #     ),
    #     NewsArticle(
    #         news_id=1,
    #         title="Apple CEO Tim Cook's 2023 Compensation Declines to $63.2 Million: Insights into Salary Structure and Future Equity Awards",
    #         content="Apple CEO Tim Cook's compensation, earnings, and stock awards have been a subject of interest and discussion among investors, analysts, and enthusiasts. This article will delve into the details of Tim Cook's earnings in 2023, his salary, stock awards, bonus awards, and other compensation. We will also explore the composition of his total earnings and the factors that influenced the decrease in his compensation compared to the previous year. Additionally, we will discuss Cook's ownership of Apple stock, RSUs, and his target equity award for the upcoming year. Furthermore, we will touch upon the earnings of other senior executives at Apple, including Luca Maestri, Kate Adams, Deirdre O'Brien, and Jeff Williams. So, let's dive right in!\n\nApple CEO Tim Cook's earnings for the year 2023 have been revealed in Apple's proxy statement. According to the statement, Tim Cook earned $63.2 million in 2023, which shows a decline compared to his earnings of $99.4 million in 2022. While this decrease might catch the attention of some observers, it is essential to understand the components that makeup Cook's total earnings to gain a comprehensive perspective.\n\nTim Cook's total earnings of $63.2 million consist of several components, including a base salary, stock awards, bonus awards, and other forms of compensation. Let's take a closer look at each of these components.\n\nIn 2023, Tim Cook received a base salary of $3 million. This base salary is a fixed component of Cook's compensation and is not subject to performance-based fluctuations.\n\nA significant portion of Tim Cook's earnings in 2023 came from stock awards, amounting to $47 million. Stock awards are a common form of compensation provided to executives to align their interests with the company's overall performance. These awards are usually granted based on various factors, such as job performance, market conditions, and shareholder approval.\n\nIn addition to his base salary and stock awards, Tim Cook received bonus awards totaling $10.7 million in 2023. These performance-based bonus awards are often tied to specific targets or milestones set by the company's board of directors and shareholders. The achievement of these targets determines the payout of the bonus awards.\n\nTim Cook's other compensation amounted to $2.5 million in 2023. This category includes several elements, such as 401(k) contributions, term life insurance premiums, vacation cash-out, security expenses, and personal air travel expenses. These additional benefits and reimbursements Apple provides are expected in executive compensation packages and aim to support the well-being and security of top-level executives.\n\nApart from his annual earnings, Tim Cook has a significant ownership stake in Apple. As of the current time, Cook owns a total of 3,280,053 shares of Apple stock. This ownership stake reflects his long-term commitment to the company's success and aligns his interests with Apple's shareholders. Furthermore, Cook possesses an additional 1,291,086 Restricted Stock Units (RSUs) that have not yet vested, meaning he will gain ownership of these shares according to a specific time-based or performance-based schedule.\n\nThe decrease in Tim Cook's compensation from $99.4 million in 2022 to $63.2 million in 2023 requires us to analyze the factors contributing to this change. It is important to note that this adjustment was not a result of underperformance or shortcomings on Cook's part but rather a conscious decision made by the board of directors, shareholders, and Cook himself.\n\nThe board of directors, shareholders, and Tim Cook decided to decrease Cook's compensation in 2023. Although Cook's target award was set at $49 million for that year, Apple's exceptional performance led to exceeding this target. Decreasing Cook's compensation was deliberately aligning the CEO's earnings with the company's overall financial performance.\n\nLooking forward to 2024, Tim Cook's target equity award has been set at $50 million. However, it is essential to note that 75 percent of this award will be subjected to performance-based vesting. This approach emphasizes the company's commitment to rewarding executives based on their contributions and results.\n\nAlongside Tim Cook, other senior executives at Apple also received substantial earnings in 2023. Executives such as Luca Maestri, Kate Adams, Deirdre O'Brien, and Jeff Williams each earned approximately $27 million, a significant portion from stock awards. This demonstrates Apple's commitment to rewarding its senior leadership team for contributing to its success.\n\nIn conclusion, Apple CEO Tim Cook earned $63.2 million in 2023, as the recently released proxy statement indicates. His earnings were composed of various elements, including a base salary, stock awards, bonus awards, and other forms of compensation. The decrease in Cook's compensation compared to the previous year can be attributed to a conscious decision made by the board of directors, shareholders, and Cook himself. Looking ahead, Cook's target equity award for 2024 is set at $50 million, with a significant portion dependent on performance-based vesting. Other senior executives at Apple earned considerable amounts, highlighting the company's commitment to rewarding top talent. With these insights, it is evident that executive compensation at Apple is closely tied to the company's performance and aims to align the interests of its leaders with those of its shareholders.",
    #         publisher="Bognor Regis News",
    #         publishedAt="2024-01-15T07:43:06Z",
    #         image_url="https://www.bognor.news/wp-content/uploads/2024/01/APPLE-__A.jpg",
    #         source_url="https://www.bognor.news/tech/apple-ceo-tim-cooks-2023-compensation-declines-to-63-2-million-insights-into-salary-structure-and-future-equity-awards/",
    #         risk_rating="low",
    #         summary="Apple CEO Tim Cook's earnings for 2023 have been revealed in Apple's proxy statement, showing a decline to $63.2 million from $99.4 million in 2022. His total earnings consist of a base salary of $3 million, stock awards of $47 million, bonus awards worth $10.7 million, and other compensation. Tim Cook's ownership of Apple stock and RSUs is significant, with a target equity award for 2024 set at $50 million. The decrease in Cook's compensation was a deliberate decision to align earnings with Apple's outstanding performance. Other Apple senior executives also received substantial earnings in 2023.",
    #         score=0,
    #         tag="",
    #     ),
    # ]

    # return {"profile": profile, "newsArticles": news_articles}
