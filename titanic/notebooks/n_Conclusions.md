## Conclusions

If someone in the White Star Line office asked us after the disaster about the approach that would best save lifes, we might be tempted to advise that they sell tickets only to aristocratic old ladies and banned young men from sailing. This answer of course illustrates that the data are merely a result of the generative process - a system that saved others by sacrificing those who were physically strongest and thus might have a chance in the water (which sadly turned out not to be the case), but also a class-based system where children of the poor were left to drown in favour of saving wealthy, elderly people.

What could be done to save more people? The data don't really tell us, they just show how, under similar circumstances, we might expect people to live or die. Moving people to first class cabins is not going to increase the survival rate, though most of the models we will come onto to discuss will predict that. 

If we truly want to learn from this data, we need meaningful features that we can take action on. For example, was the passenger wearing a life vest, were they evacuated in a lifeboat, or if not, how long did they spend in the water? Some of this information is actually available and illustrates how the insights we gain from data analysis are shaped by the sources and methods of collection.

### Science vs. Machine Learning

More generally, the aim of the scientific approach is to discover universal rules (natural laws) that apply across conditions. To identify such rules, we need systems that we can interrogate

It is possible to use ML to discover something about fundamental about a problem, if the application is well posed. For example, a system such as Google Translate find the latent space that languages share.

### Hypothesis based vs. Performance based workflows
In this repository, I've tried to work from first principles to understand the input data and extract what I believe are meaningful features for subsequent testing. This hypothesis-first approach comes from my background as a research scientist and can be compared with a different workflows that is common in machine learning that focuses on predictive performance at the outset. 

With this approach, one establishes a baseline performance first and asks how can that be beaten. In the case of the titanic dataset, the baseline is provided by Kaggle using a model based on gender that performs well. This model assumes that all women survive and all men perish. The model errors are thus cases where men survive and women perish, and so one is thus motivated to identify these cases. 
