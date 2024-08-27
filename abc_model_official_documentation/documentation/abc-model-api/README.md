---
icon: cloud-check
description: General description about API and ABC model API
---

# ABC Model API

## What is an API?

API stands for Application Programming Interface. It allows the functionalities of a web service or software to be called from another web service or software. Examples of APIs include those that fetch weather forecasts, stock information, and map data.&#x20;

Examples of representative API Services include [X API](https://developer.x.com/en/products/twitter-api), [Google Sheets API](https://developers.google.com/sheets/api/reference/rest), [YouTube Data API](https://developers.google.com/youtube/v3), and so on.

<figure><img src="../../.gitbook/assets/What-is-an-API.png" alt=""><figcaption><p>Diagram of API: An API is often compared to a waiter. It takes requests from the client (customer), retrieves the necessary information from the server (kitchen), and delivers the result back to the client.</p></figcaption></figure>

Check the video by MuleSoft Videos to learn about what APIs are in general.

{% embed url="https://www.youtube.com/watch?ab_channel=MuleSoftVideos&v=s7wmiS2mSXY" %}
An intoruductory video about API by MuleSoft Videos
{% endembed %}

## ABC Model API

ABC Model API seamlessly integrates the ABC model into third-party applications, allowing you to use its capability in your Web application or program. All you need to do is send ABC Model API an input JSON file with some simple rules setting ambient thermal parameters such as air temperature, air velocity, environmental temperature, etc. ABC Model API gets the model running with your input file and returns the comfort model's result.

{% hint style="info" %}
We use [DigitalOcean](https://www.digitalocean.com/) for this cloud computing and the URL of the ABC model API is:&#x20;

**https://fastabc-57h9n.ondigitalocean.app/abc**
{% endhint %}
