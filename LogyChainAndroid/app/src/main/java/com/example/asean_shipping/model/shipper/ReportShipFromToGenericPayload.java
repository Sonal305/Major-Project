package com.example.asean_shipping.model.shipper;
import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class ReportShipFromToGenericPayload {


    @SerializedName("contact")
    @Expose
    private String contact="";

    @SerializedName("shipmentId")
    @Expose
    private  String shipmentId;


    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }

    public String getShipmentId() {
        return shipmentId;
    }

    public void setShipmentId(String shipmentId) {
        this.shipmentId = shipmentId;
    }
}
