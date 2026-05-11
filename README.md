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




**THE UPSHOT:**

***It is not what you did. It is who the audience thought you were.***

*The Innocent Edit Score* is determined based on how thoroughly producers constructed a cast member as a 'victim' to gain audiences' sympathy 
before the cast members negative reputation incident occurs- this is the primary structural determinant of departure outcomes on Bravo programming.

**Score a New Cast Member**

Want to apply the model to a different franchise or cast member? 
Clone the repo and edit the scoring inputs in bravo_departure_model.ipynb. Each variable is documented inline.


**Methodology**

Logistic regression trained on 8 verified cases. 
Franchises selected for documented scandal involvement and confirmed departure outcomes (RHOBH, VPR, Southern Charm, Summer House). 
Model validated by correct classification of all training cases before being applied to Summer House Season 11 predictions.

Want more info? Check out my substack: (https://syntheticbeek.substack.com/p/i-built-a-model-to-predict-bravo)
