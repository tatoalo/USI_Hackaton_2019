package com.tatoalo.usihackaton2019;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.squareup.picasso.Picasso;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {//implements View.OnClickListener {

    EditText hp, xp;
    TextView levelValue;
    ProgressBar hpValue, xpValue,hpValueMonster;
    ImageButton dataBike, dataBus;
    ImageView playerImage, monsterImage;
    Spinner startData, stopData;
    static RequestQueue requestQueue;
    String hpValueString = "50", xpValueString = "50", maxValueXp = "";
    List<String> bikeAddresses = new ArrayList<>();
    List<String> busAddresses = new ArrayList<>();
    Button btnSaveData;
    EditText NO2, NO, O3, PM10;
    String dataTypeChoosen = "";
    TextView hpMonsterValue, monsterLevelValue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnSaveData = (Button) findViewById(R.id.btnSave);

        hp = (EditText) findViewById(R.id.hp);
        xp = (EditText) findViewById(R.id.xp);

        NO2 = (EditText) findViewById(R.id.NO2Value);
        NO = (EditText) findViewById(R.id.NOValue);
        O3 = (EditText) findViewById(R.id.O3Value);
        PM10 = (EditText) findViewById(R.id.PM10Value);

        hpValue = (ProgressBar) findViewById(R.id.hpValue);
        hpValueMonster = (ProgressBar) findViewById(R.id.hpValueMonster);
        xpValue = (ProgressBar) findViewById(R.id.xpValue);
        levelValue = (TextView) findViewById(R.id.levelValue);
        hpMonsterValue = (TextView) findViewById(R.id.hpMonsterValue);
        monsterLevelValue = (TextView) findViewById(R.id.monsterLvlValue);

        hp.setFocusable(false);
        xp.setFocusable(false);
        hpValue.setFocusable(false);
        hpValueMonster.setFocusable(false);
        xpValue.setFocusable(false);
        NO2.setFocusable(false);
        NO.setFocusable(false);
        O3.setFocusable(false);
        PM10.setFocusable(false);

        dataBike = (ImageButton) findViewById(R.id.dataTypeBike);
        dataBike.setImageResource(R.drawable.bike);
        dataBus = (ImageButton) findViewById(R.id.dataTypeBus);
        dataBus.setImageResource(R.drawable.bus);

        playerImage = (ImageView) findViewById(R.id.playerImg);
        monsterImage = (ImageView) findViewById(R.id.monsterImage);

        //Init Values
        hpValue.setProgress(Integer.parseInt(hpValueString), true);
        hpValueMonster.setProgress(Integer.parseInt(hpValueString), true);
        xpValue.setProgress(Integer.parseInt(xpValueString), true);

        String[] items = new String[]{"Test1", "Test2", "Test3"};

        final ArrayAdapter<String> bikeAdapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, bikeAddresses);
        final ArrayAdapter<String> busAdapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, busAddresses);
        //startData.setAdapter(adapter);
        //stopData.setAdapter(adapter);

        dataBike.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {
                dataTypeChoosen = "bike";
                dataBus.setBackgroundDrawable(dataBike.getBackground());
                dataBike.setBackgroundResource(R.drawable.btn_border);

                startData = findViewById(R.id.dataStart);
                stopData = findViewById(R.id.dataStop);

                startData.setAdapter(bikeAdapter);
                stopData.setAdapter(bikeAdapter);

            }
        });


        dataBus.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {
                dataTypeChoosen = "bus";
                dataBike.setBackgroundDrawable(dataBus.getBackground());
                dataBus.setBackgroundResource(R.drawable.btn_border);
                startData = findViewById(R.id.dataStart);
                stopData = findViewById(R.id.dataStop);

                startData.setAdapter(busAdapter);
                stopData.setAdapter(busAdapter);

            }
        });



        requestQueue= Volley.newRequestQueue(this);

        // Instantiate the RequestQueue.
        RequestQueue queue = Volley.newRequestQueue(this);
        String urlUsers = "http://10.0.2.2:5000/users/1";
        String urlBikes = "http://10.0.2.2:5000/stations/bike";
        String urlBus = "http://10.0.2.2:5000/stations/tpl";
        String urlPollution = "http://10.0.2.2:5000/pollution";
        String urlMonster = "http://10.0.2.2:5000/monsters";

        // GET USERS
        StringRequest stringRequestUsers = new StringRequest(Request.Method.GET, urlUsers,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        //System.out.println(("Here" + response));

                        try {
                            JSONObject json= (JSONObject) new JSONTokener(response).nextValue();
                            JSONObject json2 = json.getJSONObject("stats");
                            hpValueString = json2.get("hp").toString();
                            xpValueString =  json2.get("xp").toString();
                            maxValueXp =  json2.get("xp_required").toString();
                            levelValue.setText(json2.get("lvl").toString());
                            xpValue.setMax(Integer.parseInt(maxValueXp));
                            hpValue.setProgress(Integer.parseInt(hpValueString), true);
                            xpValue.setProgress(Integer.parseInt(xpValueString), true);
                            String urlImage = (String) json.get("icon");
                            Picasso.get().load(urlImage).into(playerImage);

                            //JSONObject currentFight = (JSONObject) json.getJSONObject("user").get("current_fight");
                            //hpValueMonster.setProgress(Integer.parseInt(hpValueString), true);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });

        // GET MONSTERS
        StringRequest stringRequestMonster = new StringRequest(Request.Method.GET, urlMonster,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        try {
                            //JSONObject json= (JSONObject) new JSONTokener(response).nextValue();
                            //JSONObject json2 = json.getJSONObject("id");
                            JSONArray json = new JSONArray(response);


                            hpMonsterValue.setText(json.getJSONObject(0).get("max_hp").toString());
                            monsterLevelValue.setText(json.getJSONObject(0).get("lvl").toString());

                            String urlImage = json.getJSONObject(0).get("icon").toString();
                            Picasso.get().load(urlImage).into(monsterImage);
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });


        //GET BIKES
        StringRequest stringRequestBikes = new StringRequest(Request.Method.GET, urlBikes,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        int count = 0;
                            try {
                                JSONArray json = new JSONArray(response);

                                while(count < json.length()){
                                    //System.out.println(json.getJSONObject(count).get("address"));
                                    bikeAddresses.add(json.getJSONObject(count).get("name").toString());
                                    count++;
                                }

                            } catch (JSONException e) {
                                e.printStackTrace();
                            }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });

        //GETBUS
        StringRequest stringRequestBus = new StringRequest(Request.Method.GET, urlBus,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        int count = 0;


                        try {
                            JSONArray json = new JSONArray(response);
                            //System.out.println(json.getJSONObject(count));

                            while(count < json.length()){
                                //System.out.println(json.getJSONObject(count).get("address"));
                                busAddresses.add(json.getJSONObject(count).get("name").toString());
                                count++;
                            }

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });

        //GETPollution
        StringRequest stringRequestPollution = new StringRequest(Request.Method.GET, urlPollution,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        int count = 0;

                        try {
                            JSONObject json= (JSONObject) new JSONTokener(response).nextValue();
                            System.out.println("Pollution: " + json.get("NO2"));
                            NO2.setText(json.get("NO2").toString());
                            NO.setText(json.get("NO").toString());
                            O3.setText(json.get("O3").toString());
                            PM10.setText(json.get("PM10").toString());
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }



                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });

        //POSTSaveButton




        //
        btnSaveData.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {
                getFigthResult();
            }
        });

        // Add the request to the RequestQueue.
        queue.add(stringRequestBus);
        queue.add(stringRequestUsers);
        queue.add(stringRequestBikes);
        queue.add(stringRequestPollution);
        queue.add(stringRequestMonster);



    }

    public String[] getInfo(String url){
        RequestQueue queue = Volley.newRequestQueue(this);
        final String[] info = new String[5];

        System.out.print("ASDFGHJKL;SXCVBNFGHGFDFBNMJHGFGHJH"+url);
        StringRequest stringRequestBikeDetails = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {
                        int count = 0;
                        try {
                            //JSONArray json = new JSONArray(response);
                            JSONObject json= (JSONObject) new JSONTokener(response).nextValue();
                            info[0] = json.get("id").toString();
                            info[1] = json.get("name").toString();

                            try {
                                info[2] = json.get("address").toString();
                            }catch(Exception e){
                                info[2] = "";
                            }
                            String temp = json.get("coords").toString();
                            String[] parts = temp.split("\"");

                            info[3] = parts[3];
                            info[4] = parts[7];


                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });
        queue.add(stringRequestBikeDetails);

        return info;
    }

    public void getFigthResult() {

        final String urlSaveButton = "http://10.0.2.2:5000/users/1";
        RequestQueue queue = Volley.newRequestQueue(this);
        JsonObjectRequest jsonOblect = null;
        try {
            String URL = urlSaveButton;
            JSONObject jsonBody = new JSONObject();

            String urlStart = "";
            String urlEnd = "";
            switch(dataTypeChoosen){
                case "bus":
                    urlStart = "http://10.0.2.2:5000/stations/tpl/" + startData.getSelectedItem().toString();
                    urlEnd = "http://10.0.2.2:5000/stations/tpl/" + stopData.getSelectedItem().toString();
                    break;
                case "bike":
                    urlStart = "http://10.0.2.2:5000/stations/bike/" + startData.getSelectedItem().toString();
                    urlEnd = "http://10.0.2.2:5000/stations/bike/" + stopData.getSelectedItem().toString();
                    break;
            }


            String[] info_start = getInfo(urlStart);
            String[] info_end = getInfo(urlEnd);

            //
            //le coordinate soono tutto nulle
            //quindi info start e info end provengono dal metodo getInfo
            //
            //

            info_start[3] = "45.953905";
            info_start[4] = "8.949715";
            info_end[3] = "45.9242";
            info_end[4] = "8.9192";


            System.out.println("CIAOOOOO"+ info_start[3]+info_start[4]+info_end[3]+info_end[4]);
            jsonBody.put("type", dataTypeChoosen);
            jsonBody.put("lat_start", info_start[3]);
            jsonBody.put("lon_start", info_start[4]);
            jsonBody.put("lat_end", info_end[3]);
            jsonBody.put("lon_end", info_end[4]);

            jsonOblect = new JsonObjectRequest(Request.Method.PUT, URL, jsonBody, new Response.Listener<JSONObject>() {
                @Override
                public void onResponse(JSONObject response) {

                    try {
                        System.out.println("ASDASDADADASDASD");
                        JSONObject json= (JSONObject) new JSONTokener(response.toString()).nextValue();

                        System.out.println("RESPONSE: " + response);

                        JSONObject stats = (JSONObject) json.getJSONObject("user").get("stats");
                        JSONObject currentFight = (JSONObject) json.getJSONObject("user").get("current_fight");
                        JSONObject monster = (JSONObject) json.getJSONObject("monster");
                        hpValueString = stats.get("hp").toString();
                        xpValueString = stats.get("xp").toString();
                        maxValueXp = stats.get("xp_required").toString();

                        xpValue.setMax(Integer.valueOf(maxValueXp));

                        levelValue.setText(stats.get("lvl").toString());
                        hpValue.setProgress(Integer.valueOf(hpValueString), true);
                        xpValue.setProgress(Integer.valueOf(xpValueString), true);
                        hpMonsterValue.setText(currentFight.get("monster_hp").toString());

                        monsterLevelValue.setText(monster.get("lvl").toString());

                        String urlImage = monster.get("icon").toString();
                        Picasso.get().load(urlImage).into(monsterImage);


                    } catch (JSONException e) {
                        e.printStackTrace();
                    }

                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    onBackPressed();
                }
            });

        } catch (JSONException e) {
            e.printStackTrace();
        }
        queue.add(jsonOblect);
    }

}



