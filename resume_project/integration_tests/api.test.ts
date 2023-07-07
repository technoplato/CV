import axios from "axios";

describe("API Tests", () => {
  it("should get a response from the API", async () => {
    try {
      const response = await axios.post(
        "http://api:4000/",
        {
          query: `
            {
              __schema {
                types {
                  name
                }
              }
            }
          `,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      console.log("Response data:", JSON.stringify(response.data, null, 2));
    } catch (error) {
      if (error.response) {
        console.error(
          "Error making request: ",
          error.response.status,
          error.response.statusText
        );
        console.error("Error data: ", error.response.data);
      } else {
        console.error("Error making request: ", error.message);
      }
    }
  });
});
