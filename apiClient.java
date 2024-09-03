package LostVegasAPI;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

public class ApiClient {

    private static final String BASE_URL = "http://localhost:8000";  // Replace with your FastAPI server URL

    /**
     * Available Endpoints:
     * 
     * GM Endpoints:
     * 1. POST /gm/add-character
     *    - Function: addCharacter
     *    - Description: Adds a new character.
     * 
     * 2. POST /gm/add-ability
     *    - Function: addAbility
     *    - Description: Adds a new ability.
     * 
     * 3. POST /gm/add-expertise
     *    - Function: addExpertise
     *    - Description: Adds a new expertise.
     * 
     * 4. POST /gm/add-job-skill
     *    - Function: addJobSkill
     *    - Description: Adds a new job skill.
     * 
     * 5. POST /gm/add-species-passive
     *    - Function: addSpeciesPassive
     *    - Description: Adds a new species passive.
     * 
     * 6. POST /gm/add-item
     *    - Function: addItem
     *    - Description: Adds a new item.
     * 
     * 7. POST /gm/add-weapon
     *    - Function: addWeapon
     *    - Description: Adds a new weapon.
     * 
     * 8. GET /gm/view-characters
     *    - Function: viewCharacters
     *    - Description: Retrieves all characters.
     * 
     * 9. GET /gm/view-libraries
     *    - Function: viewLibraries
     *    - Description: Retrieves all libraries.
     * 
     * 10. GET /gm/view-backpacks
     *    - Function: viewBackpacks
     *    - Description: Retrieves all backpacks.
     * 
     * 11. GET /gm/view-items
     *    - Function: viewItems
     *    - Description: Retrieves all items.
     * 
     * 12. GET /gm/view-abilities
     *    - Function: viewAbilities
     *    - Description: Retrieves all abilities.
     * 
     * 13. DELETE /gm/remove-items
     *    - Function: bulkRemoveItems
     *    - Description: Removes items based on criteria.
     * 
     * Player and GM Endpoints:
     * 14. POST /player/add-character
     *    - Function: addPlayerCharacter
     *    - Description: Adds a new player character.
     * 
     * 15. GET /player/view-character
     *    - Function: viewPlayerCharacter
     *    - Description: Retrieves all characters for a player.
     * 
     * 16. GET /player/view-backpack
     *    - Function: viewPlayerBackpack
     *    - Description: Retrieves a player's backpack.
     * 
     * 17. GET /player/view-library
     *    - Function: viewPlayerLibrary
     *    - Description: Retrieves a player's library.
     * 
     * 18. GET /player/get-ability
     *    - Function: getAbilityDetails
     *    - Description: Retrieves details of a specific ability.
     * 
     * 19. GET /player/get-job-skill
     *    - Function: getJobSkillDetails
     *    - Description: Retrieves details of a specific job skill.
     * 
     * 20. GET /player/get-species-passive
     *    - Function: getSpeciesPassiveDetails
     *    - Description: Retrieves details of a specific species passive.
     * 
     * 21. GET /player/get-expertise
     *    - Function: getExpertiseDetails
     *    - Description: Retrieves details of a specific expertise.
     * 
     * 22. GET /player/get-item
     *    - Function: getItemDetails
     *    - Description: Retrieves details of a specific item.
     * 
     * 23. GET /player/get-weapon
     *    - Function: getWeaponDetails
     *    - Description: Retrieves details of a specific weapon.
     * 
     * 24. POST /player/level-up
     *    - Function: levelUpCharacter
     *    - Description: Levels up a character.
     * 
     * 25. POST /player/adjust-stats
     *    - Function: adjustCharacterStats
     *    - Description: Adjusts character stats.
     * 
     * 26. POST /player/add-item
     *    - Function: addItemToBackpack
     *    - Description: Adds an item to a player's backpack.
     * 
     * 27. DELETE /player/remove-item
     *    - Function: removeItemFromBackpack
     *    - Description: Removes an item from a player's backpack.
     * 
     * 28. POST /player/add-weapon
     *    - Function: addWeaponToBackpack
     *    - Description: Adds a weapon to a player's backpack.
     * 
     * 29. DELETE /player/remove-weapon
     *    - Function: removeWeaponFromBackpack
     *    - Description: Removes a weapon from a player's backpack.
     */

    // GM Endpoints

    public String addCharacter(Map<String, Object> charData) throws Exception {
        String endpoint = BASE_URL + "/gm/add-character/";
        String jsonInputString = new JSONObject(charData).toString();
        return postResponse(endpoint, jsonInputString);
    }

    public String addAbility(Map<String, Object> abilityData) throws Exception {
        String endpoint = BASE_URL + "/gm/add-ability/";
        String jsonInputString = new JSONObject(abilityData).toString();
        return postResponse(endpoint, jsonInputString);
    }

    public String addExpertise(Map<String, Object> expertiseData) throws Exception {
        String endpoint = BASE_URL + "/gm/add-expertise/";
        String jsonInputString = new JSONObject(expertiseData).toString();
        return postResponse(endpoint, jsonInputString);
    }

    public String addJobSkill(Map<String, Object> jobSkillData) throws Exception {
        String endpoint = BASE_URL + "/gm/add-job-skill/";
        String jsonInputString = new JSONObject(jobSkillData).toString();
        return postResponse(endpoint, jsonInputString);
    }

    public String addSpeciesPassive(Map<String, Object> speciesPassiveData) throws Exception {
        String endpoint = BASE_URL + "/gm/add-species-passive/";
        String jsonInputString = new JSONObject(speciesPassiveData).toString();
        return postResponse(endpoint, jsonInputString);
    }

    public String addItem(Map<String, Object> itemData) throws Exception {
        String endpoint = BASE_URL + "/gm/add-item/";
        String jsonInputString = new JSONObject(itemData).toString();
        return postResponse(endpoint, jsonInputString);
    }

    public String addWeapon(Map<String, Object> weaponData) throws Exception {
        String endpoint = BASE_URL + "/gm/add-weapon/";
        String jsonInputString = new JSONObject(weaponData).toString();
        return postResponse(endpoint, jsonInputString);
    }

    public String viewCharacters() throws Exception {
        String endpoint = BASE_URL + "/gm/view-characters/";
        return getResponse(endpoint);
    }

    public String viewLibraries() throws Exception {
        String endpoint = BASE_URL + "/gm/view-libraries/";
        return getResponse(endpoint);
    }

    public String viewBackpacks() throws Exception {
        String endpoint = BASE_URL + "/gm/view-backpacks/";
        return getResponse(endpoint);
    }

    public String viewItems() throws Exception {
        String endpoint = BASE_URL + "/gm/view-items/";
        return getResponse(endpoint);
    }

    public String viewAbilities() throws Exception {
        String endpoint = BASE_URL + "/gm/view-abilities/";
        return getResponse(endpoint);
    }

    public String bulkRemoveItems(Map<String, Object> removeCriteria) throws Exception {
        String endpoint = BASE_URL + "/gm/remove-items/";
        String jsonInputString = new JSONObject(removeCriteria).toString();
        return deleteResponse(endpoint, jsonInputString);
    }

    // Player and GM Endpoints

    public String addPlayerCharacter(Map<String, Object> charData) throws Exception {
        String endpoint = BASE_URL + "/player/add-character/";
        String jsonInputString = new JSONObject(charData).toString();
        return postResponse(endpoint, jsonInputString);
    }

    public String viewPlayerCharacter(int userId) throws Exception {
        String endpoint = BASE_URL + "/player/view-character/?user_id=" + userId;
        return getResponse(endpoint);
    }

    public String viewPlayerBackpack(int charId) throws Exception {
        String endpoint = BASE_URL + "/player/view-backpack/?char_id=" + charId;
        return getResponse(endpoint);
    }

    public String viewPlayerLibrary(int charId) throws Exception {
        String endpoint = BASE_URL + "/player/view-library/?char_id=" + charId;
        return getResponse(endpoint);
    }

    public String getAbilityDetails(int abilityId) throws Exception {
        String endpoint = BASE_URL + "/player/get-ability/?ability_id=" + abilityId;
        return getResponse(endpoint);
    }

    public String getJobSkillDetails(int jobSkillId) throws Exception {
        String endpoint = BASE_URL + "/player/get-job-skill/?job_skill_id=" + jobSkillId;
        return getResponse(endpoint);
    }

    public String getSpeciesPassiveDetails(int speciesPassiveId) throws Exception {
        String endpoint = BASE_URL + "/player/get-species-passive/?species_passive_id=" + speciesPassiveId;
        return getResponse(endpoint);
    }

    public String getExpertiseDetails(int expertiseId) throws Exception {
        String endpoint = BASE_URL + "/player/get-expertise/?expertise_id=" + expertiseId;
        return getResponse(endpoint);
    }

    public String getItemDetails(int itemId) throws Exception {
        String endpoint = BASE_URL + "/player/get-item/?item_id=" + itemId;
        return getResponse(endpoint);
    }

    public String getWeaponDetails(int weaponId) throws Exception {
        String endpoint = BASE_URL + "/player/get-weapon/?weapon_id=" + weaponId;
        return getResponse(endpoint);
    }

    public String levelUpCharacter(int charId, int newLevel) throws Exception {
        String endpoint = BASE_URL + "/player/level-up/";
        String jsonInputString = "{\"char_id\": " + charId + ", \"new_level\": " + newLevel + "}";
        return postResponse(endpoint, jsonInputString);
    }

    public String adjustCharacterStats(Map<String, Object> statsData, Map<String, Integer> statAllocation, int rolledValue) throws Exception {
        String endpoint = BASE_URL + "/player/adjust-stats/";
        
        // Define max limits for the stats
        int maxStatLimit = 50;
        int totalAllocation = 0;
    
        // Validate the stat allocations
        for (int allocation : statAllocation.values()) {
            totalAllocation += allocation;
        }
    
        if (totalAllocation > rolledValue) {
            throw new Exception("Total allocation exceeds rolled value.");
        }
    
        // Adjust stats based on the provided allocation
        for (String stat : statAllocation.keySet()) {
            if (statsData.get(stat) instanceof Integer) {
                int currentStat = (Integer) statsData.get(stat);
                int allocation = statAllocation.get(stat);
                int newStat = currentStat + allocation;
    
                // Ensure the new stat doesn't exceed the max limit
                if (newStat > maxStatLimit) {
                    newStat = maxStatLimit;
                }
    
                statsData.put(stat, newStat);
            }
        }
    
        // Convert the adjusted stats to JSON
        String jsonInputString = new JSONObject(statsData).toString();
        
        // Logging the adjusted stats and allocation
        System.out.println("Adjusting stats with the following data: " + jsonInputString);
    
        return postResponse(endpoint, jsonInputString);
    }

    public String addItemToBackpack(int charId, int itemId) throws Exception {
        String endpoint = BASE_URL + "/player/add-item/";
        String jsonInputString = "{\"char_id\": " + charId + ", \"item_id\": " + itemId + "}";
        return postResponse(endpoint, jsonInputString);
    }

    public String removeItemFromBackpack(int charId, int itemId) throws Exception {
        String endpoint = BASE_URL + "/player/remove-item/?char_id=" + charId + "&item_id=" + itemId;
        return deleteResponse(endpoint, "");
    }

    public String addWeaponToBackpack(int charId, int weaponId) throws Exception {
        String endpoint = BASE_URL + "/player/add-weapon/";
        String jsonInputString = "{\"char_id\": " + charId + ", \"weapon_id\": " + weaponId + "}";
        return postResponse(endpoint, jsonInputString);
    }

    public String removeWeaponFromBackpack(int charId, int weaponId) throws Exception {
        String endpoint = BASE_URL + "/player/remove-weapon/?char_id=" + charId + "&weapon_id=" + weaponId;
        return deleteResponse(endpoint, "");
    }

    // HTTP request methods

    private String getResponse(String endpoint) throws Exception {
        URL url = new URL(endpoint);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("GET");

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            return response.toString();
        } else {
            throw new Exception("GET request failed. Response Code: " + responseCode);
        }
    }

    private String postResponse(String endpoint, String jsonInputString) throws Exception {
        URL url = new URL(endpoint);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("POST");
        connection.setRequestProperty("Content-Type", "application/json; utf-8");
        connection.setDoOutput(true);

        try (OutputStream os = connection.getOutputStream()) {
            byte[] input = jsonInputString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream(), "utf-8"));
            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine.trim());
            }
            in.close();

            return response.toString();
        } else {
            throw new Exception("POST request failed. Response Code: " + responseCode);
        }
    }

    private String deleteResponse(String endpoint, String jsonInputString) throws Exception {
        URL url = new URL(endpoint);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod("DELETE");
        connection.setRequestProperty("Content-Type", "application/json; utf-8");
        connection.setDoOutput(true);

        try (OutputStream os = connection.getOutputStream()) {
            byte[] input = jsonInputString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        int responseCode = connection.getResponseCode();
        if (responseCode == HttpURLConnection.HTTP_OK) { // success
            BufferedReader in = new BufferedReader(new InputStreamReader(connection.getInputStream(), "utf-8"));
            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine.trim());
            }
            in.close();

            return response.toString();
        } else {
            throw new Exception("DELETE request failed. Response Code: " + responseCode);
        }
    }

    private Map<String, Object> parseJsonResponse(String jsonResponse) {
        JSONObject jsonObject = new JSONObject(jsonResponse);
        Map<String, Object> resultMap = new HashMap<>();

        for (String key : jsonObject.keySet()) {
            Object value = jsonObject.get(key);
            resultMap.put(key, value);
        }

        return resultMap;
    }
}