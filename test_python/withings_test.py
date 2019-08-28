from withings import WithingsAuth, WithingsApi

auth = WithingsAuth("2673d8c4a99e458a23ee3d7091a38b15f31139a4c4f29e74c5f300b9d31c6d47", "d1272b6379460a976aa0411e451c8255db1323c2b64f94b51d173b85088fea76")
authorize_url = auth.get_authorize_url()
print("Go to %s allow the app and copy your oauth_verifier" % authorize_url)

# oauth_verifier = raw_input('Please enter your oauth_verifier: ')
# creds = auth.get_credentials(oauth_verifier)
#
# client = WithingsApi(creds)
# measures = client.get_measures(limit=1)
# print("Your last measured weight: %skg" % measures[0].weight)