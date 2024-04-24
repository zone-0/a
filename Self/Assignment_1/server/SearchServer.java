package server;

import remotes.SearchQuery;
import remotes.Search;

import java.rmi.*;
import java.rmi.registry.*;

public class SearchServer {
    public static void main(String[] args) {
        try {
            Search search = new SearchQuery();
            String url = "rmi://localhost:1099/REMOTE_SEARCH";
            LocateRegistry.createRegistry(1099);
            Naming.rebind(url, search);
            System.out.("Search Server ready");
        } catch (Exception e) {
            System.out.println("Error in creating server");
        }
    }println
}
