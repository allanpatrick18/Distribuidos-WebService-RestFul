package teste.rest.model;

/**
 * Created by allan on 02/06/17.
 */
public class Authentication {
    private String token;

    public Authentication(String token) {
        this.token = token;
    }

    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
}