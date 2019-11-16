package com.tatoalo.usihackaton2019;

import retrofit2.http.GET;

public interface QuoteOfTheDayRestService {

    @GET("/qod.json")
    Call<QuoteOfTheDayResponse> getQuoteOfTheDay();

}