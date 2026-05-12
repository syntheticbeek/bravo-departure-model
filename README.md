**Bravo Departure Index**
A logistic regression model for predicting cast departures across Bravo reality franchises.

**Background**

Departure outcomes on Bravo are not random. They follow a pattern and patterns can be modeled.

I defined eight variables, scored them across eight documented scandal cases from four franchises, trained a logistic regression model, 
and applied it to predict outcomes for Amanda Batula and West Wilson following the Summer House Post-Season 10 scandal.

**The Model Results**

96.9% cast departure probability for Amanda Batula


3.4% cast departure probability for West Wilson


Same incident. Same show. Same season. 93.6 pt difference.

**8 Variables Defined:**

<img width="630" height="521" alt="Screenshot 2026-05-10 at 7 56 44 PM" src="https://github.com/user-attachments/assets/101cb84e-ae45-4119-b95d-526c68645cd9" />


**Training Data**

Eight cases across four franchises with verified departure outcomes.

<img width="454" height="389" alt="Screenshot 2026-05-10 at 9 28 38 PM" src="https://github.com/user-attachments/assets/0e768ad3-bbba-4040-8edd-93bd7758ec00" />


**Predictions: Summer House Season 11**

<img width="315" height="82" alt="Screenshot 2026-05-10 at 9 30 29 PM" src="https://github.com/user-attachments/assets/7f68f0bf-0e79-405a-9313-1d0a7e2455ce" />


**Ablation Analysis**

To isolate what drives the 93.6 point gap (calculated from raw model output), I retrained the model three times 
each time removing one variable.

<img width="390" height="97" alt="Screenshot 2026-05-10 at 9 31 06 PM" src="https://github.com/user-attachments/assets/b2f6d817-9d63-4c94-9ab4-49a9d8ddaa20" />



**Permutation Test**

The outcome labels were randomly shuffled 10,000 times and the model retrained on each permutation. Only 256 of 10,000 random configurations produced a gap as large as the observed 93.6%. The mean gap under random conditions was 40.4%.

P-value: 0.0256

The observed gap is statistically significant at the 0.05 threshold. The finding is unlikely to be a product of random chance despite the small sample size.

**THE UPSHOT:**

***It is not what you did. It is who the audience thought you were.***

*The Innocent Edit Score* is determined based on how thoroughly producers constructed a cast member as a 'victim' to gain audiences' sympathy 
before the cast members negative reputation incident occurs- this is the primary structural determinant of departure outcomes on Bravo programming.

**Score a New Cast Member**

Want to apply the model to a different franchise or cast member? 
Clone the repo and edit the scoring inputs in BRAVO_CASTMATE_DEPARTURE.ipynb . Each variable is documented inline.


**Methodology**

Logistic regression trained on eight verified cases across four Bravo franchises (Real Housewives of Beverly Hills, Vanderpump Rules, Southern Charm, and Summer House). Cases were selected based on documented scandal involvement and confirmed departure outcomes. All variable scores were assigned by the researcher based on direct observation of available footage and established Bravo narrative conventions.


Want more info? Check out my substack: (https://syntheticbeek.substack.com/p/i-built-a-model-to-predict-bravo)

