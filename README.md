**Bravo Departure Index**
A logistic regression model for predicting cast departures across Bravo reality franchises.

**Background**

Departure outcomes on Bravo are not random. They follow a pattern and patterns can be modeled.

I defined eight variables, scored them across eight documented scandal cases from four franchises, trained a logistic regression model, 
and applied it to predict outcomes for Amanda Batula and West Wilson following the Summer House Post-Season 10 scandal.

**The Model Results**

96.9% cast departure probability for Amanda Batula
2.8% cast departure probability for West Wilson
Same incident. Same show. Same season. 94.1 points apart.
*(See Full write-up: syntheticbeek.substack.com)*

**8 Variables Defined:**

<img width="630" height="521" alt="Screenshot 2026-05-10 at 7 56 44 PM" src="https://github.com/user-attachments/assets/101cb84e-ae45-4119-b95d-526c68645cd9" />

Removing gender changes almost nothing (−0.1 pts). 
Removing the betrayal index reduces the gap by 11.4 points. 
Removing the victim narrative variable collapses the gap by 58.9 points (nearly two thirds of the model's total predictive power).

**Training Data**

Eight cases across four franchises with verified departure outcomes.

<img width="625" height="326" alt="Screenshot 2026-05-10 at 8 37 12 PM" src="https://github.com/user-attachments/assets/43ac4b0e-e855-414f-8ffa-095f952fc33b" />


**Predictions: Summer House Season 11**

<img width="632" height="111" alt="Screenshot 2026-05-10 at 7 57 46 PM" src="https://github.com/user-attachments/assets/a25331a1-d48c-4c64-84fa-1d3837fb5d4a" />


**Ablation Analysis**

To isolate what drives the 94.1-point gap, I retrained the model three times 
each time removing one variable.

<img width="340" height="165" alt="Screenshot 2026-05-10 at 8 06 04 PM" src="https://github.com/user-attachments/assets/0368984a-eb18-4483-875b-5becd387de7e" />

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
