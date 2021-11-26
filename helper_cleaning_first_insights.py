import pandas as pd
from collections import Counter


''' 
this function gives an overview about the percantage of NaN values in a dataframe 
'''
def percantage_null(data):
    nulls = pd.DataFrame(data.isna().sum()*100/len(data), columns=['percentage'])
    print(nulls.sort_values('percentage', ascending = False))


''' 
this function gives an overview about the frequency of a value in every column of a dataframe 
input is a dataframe
output is a print of value counts  
'''
def value_counts(data):
    for col in data:
        print(data[col].value_counts(), '\n')    
    
    
''' 
this function showes the unique value of one column of a dataframe
input is the name of a column 
output is a print of unique values  
'''
def show_unique_values(df, column_name):
    uniques = df[column_name].unique()
    uniques_list = []
    for i in uniques: 
        uniques_list.append(str(i))
    for x in sorted(uniques_list):
        print(x)
    

''' 
this function showes the valuecount of a column without a maximum of rows
input is the name of a dataframe and a column 
output is a print of unique values without maximum 
'''
def df_value_counts(df,column): 
    column_values = df[column].value_counts()
    pd.set_option("max_rows", None)
    return pd.DataFrame(column_values)
    
    
    
''' 
this function gives us the first value of a column with several values 
input is a column with several  values 
output is the input column with only the first value 
'''    
def take_first_value(df, column): 
    df_scope = df[column].str.split(' ', n=1, expand=True) 
    df_scope_list = df_scope[0]
    df_scope_list_new = [] 
    for i in df_scope_list: 
        df_scope_list_new.append(str(i).replace(",",""))
    df[column] = df_scope_list_new

  

''' 
this function clean the price column 
input is a column with several  prices
output is the input column with only one price and a clear format
'''        
def clean_price(df, column):
    df_price = df[column].str.split(' ', n=1, expand=True) 

    df_price_list = df_price[0]
    df_price_list_new = []

    for i in df_price_list: 
        df_price_list_new.append(str(i).replace(",", "."))
    
    df[column] = pd.to_numeric(df_price_list_new, errors='coerce')
    return df[column]



''' 
this function clean the size column 
input is a column with several  sizes
output is the input column with only a cleaned format
'''        
def clean_size(df, column): 
    sizes_new = []
    sizes = df[column]

    for i in sizes: 
        if "Stk" in (str(i)) and len(str(i)) < 7:  
            i = i.replace("Stk", "").replace(" ", "").replace(".", "")
            if len(str(i)) > 0: 
                i = int(i)
                i = i*100 
                sizes_new.append(str(i))
            else: 
                sizes_new.append(str(i))
        else: 
            sizes_new.append(str(i).replace("g",""))

    df[column] = sizes_new

    sizes_new_new = []
    sizes = df[column]

    for i in sizes: 
        if len(str(i)) > 5 or is_number(i) == False:  
            sizes_new.append("Null")
        else: 
            sizes_new.append(str(i))

    df[column] = sizes_new_new
    return df[column]





''' 
this function clean the category column 
input is a column with several a lot of different categories and a list of values I want to replace by the most common value 
output is the input column with only five main categories
'''            
def clean_category_stay(df, column, list_to_stay):

    category_list = df[column].to_list()
    new_category_list = []
    most_frequent_value = df[column].value_counts()[:1].index

    for i in category_list: 
        if i not in list_to_stay: 
            new_category_list.append(most_frequent_value[0])
        else: 
            new_category_list.append(i)

    df[column] = new_category_list
    
    
''' 
this function clean the age column 
input is a column with different age values
output is the input column with cleaned values 
'''                
def clean_age(df, column): 
    
    age_list = df[column].to_list()
    age_list_new = []

    for i in age_list:
        if "Baby" in str(i): 
            age_list_new.append('0')
        elif "Kind" in str(i): 
            age_list_new.append('4')
        elif "Teenager" in str(i): 
            age_list_new.append('13')
        elif "20+" in str(i): 
            age_list_new.append('20')
        elif "30" in str(i): 
            age_list_new.append('30')
        elif "40" in str(i): 
            age_list_new.append('40')
        elif "50" in str(i): 
            age_list_new.append('50')
        elif i == "Null" or "Alle" in str(i): 
            age_list_new.append('100')
        else: 
            age_list_new.append('100')
    
    return df[column] = age_list_new  
    
    
''' 
this function clean the scope column 
input is a column with different scope values
output is the first scope from the input column with cleaned, summarized values
'''           
def clean_scope(df, column): 
    df[column] = df[column].str.split(' ', n=1, expand=True) 
    new_scope = []
    list_scope = df[column].to_list()

    for i in list_scope: 
        new_scope.append(str(i).replace("FüÃŸe", "Füße").replace("Null", "Körper").replace("None", "Körper").replace(",",""))

    df[column] = new_scope 
    scope_list_2 = df[column].to_list()
    scope_list_new = []


    for i in scope_list_2:
        if i in ["Dekolleté"]: 
            scope_list_new.append('Hals')
        elif i in ["Lippen","Oberlippe"]: 
            scope_list_new.append('Mund')
        elif i in ["Kopfhaut"]: 
            scope_list_new.append('Haare')
        elif i in ["Badezimmer", 'Intimbereich', "nan", "Schlafzimmer"]: 
            scope_list_new.append('Everywhere')
        elif i in ["Nagelhaut"]: 
            scope_list_new.append('Hände')
        elif i in ["Ohren", "Kinn"]: 
            scope_list_new.append('Gesicht')
        elif i in ["Arme", 'Füße']: 
            scope_list_new.append('Körper')
        else: 
            scope_list_new.append(i)
    
    return df[column] = scope_list_new
    
    
    
    
''' 
this function clean the charesteristics column
input is a column with a lot of different charesteristics and a list with the values that should be encoded 
output is a dataframe with binary columns for every charesteristic that i in the to_stay list
'''      
def clean_charesteristics(df, column, to_stay_list):
    chara_list = df[column].to_list()


    for a in to_stay:
        b_count = []
        for i in chara_list:
            if a in i:
                b_count.append("1")
            elif a not in i:
                b_count.append("0")
        df[("char_" + a)]  = b_count
    return df
    
    
''' 
this function clean the product_award column
input is a column with a lot of different awards and a list with the values that should be encoded 
output is a dataframe with binary columns for every award that i in the to_stay list
'''     
def clean_award(df, column, to_stay_list: 
    awa_list = df["product_award"].to_list()

    df['product_award'] = df['product_award'].astype(str)
    for c in to_stay:
        d_count = []
        for i in awa_list:
            if c in i:
                d_count.append("1")
            elif c not in i:
                d_count.append("0")
        df[("awa_" + c)]  = d_count    
    return df 
    
    
    
''' 
this function clean the effect column
input is a column with a lot of different effects and a list with the values that should be encoded 
output is a dataframe with binary columns for every effect that i in the to_stay list
'''     
def clean_effect(df, column, to_stay_list):
    effect_list = df[column].to_list()
    new_effect = []

    for i in effect_list: 
        if i in ["bändigend", "schwungfixierend"]: 
            new_effect.append("formend")
        elif i in ["glitzernd","schimmernd", "leuchtend"]: 
            new_effect.append("glanzverleihend")
        elif i in ["volumengebend"]: 
            new_effect.append("volumenverstärkend")
        else: 
            new_effect.append(i)
        
    df[column] = new_effect
    df[column] = df[column].astype(str)
    eff_list = df[column].to_list()

    for c in to_stay:
        d_count = []
        for i in eff_list:
            if c in i:
                d_count.append("1")
            elif c not in i:
                d_count.append("0")
        df[("eff_" + c)]  = d_count
    return df 
    
    
''' 
this function clean the type column
input is a column with a lot of different types 
output is the input column with only 50 main types
'''     
def clean_type(df, column):

    type_list = df[column].to_list()
    type_list_new = []
    
    for i in type_list:
        if i in ["Reinigungspuder", 'Reinigungspads',"Reinigungscreme",'Make-up Entferner', "Reinigungsschaum",      
                'Reinigungspuder','Reinigungsoel', 'Reinigungsgel', 'Reinigungsmilch',               
                 'Gebissreiniger','Reinigungsstick','Reinigungsspray', 'Reinigungsinstrument', 'Wascherde', 'Gesichtskur']: 
            type_list_new.append('Gesichtsreinigung')
        elif i in ["Uhr", "Armreif", "Haarschmuck", 'Armband','Halskette', 'Ohrring', 'Tattoo', "Ring"]: 
            type_list_new.append('Schmuck')
        elif i in ['Babyshampoo', 'Volumenspray', 'Haarspülung', 'Kopfhautpeeling', 'Haarpuder']: 
            type_list_new.append('Haarshampoo')
        elif i in ["Haarstyling-Liquid", 'Haarcreme', 'Glanzspray', 'Haarvitamine', 'Haarspray', 'Haarfarbe', 
                "Haarpflege",  'Haargel', 'Haarparfum', 'Trockenshampoo','Kopfhautpflege', 'Haarserum', 'Haarschaum',
                'Haarwachs', 'Haarkur', "Haaröl", "Haarfluid", "Hitzeschutzspray"]: 
            type_list_new.append('Haarprodukt')
        elif i in ["Detangler", "Reiseset", "Schwamm", 'Fieberthermometer', 'Pflege-Accessoires', 'Bürsten & Kämme', 
               'Desinfektionsmittel','Anspitzer','Erfrischungstuch','Haartrockner', 'Trimmer', 'Stylingprodukt',
               'Extensions', 'Nagelhautentferner',  'Hornhautentferner','Lockenstyler', 'Nageldesign','Haarglätter',
               'Nagelschere', 'Mikro Needle Roller', 'Applikator','Haarschneider', 'Make up Accessoires', 'Pinzette']: 
            type_list_new.append('Beautytools')
        elif i in ['Socken','Schuh-Deo', "Etui", 'Haarband','Schuhe', 'Gürtel', 'Geldbörse',  'Haarspange', 'Haargummi',
               "Haarreif", 'Kosmetikkoffer',  'Beauty Case','Haarclips', 'Lockenwickler', 'Haarklammer', 'Stirnband',
               'Handschuhe', 'Tasche', 'Augenbinde', 'Rucksack', 'Kosmetiktasche', 'Kulturtasche','Bauchtasche', 
               'Laptoptasche', 'Bauchtasche' ]: 
            type_list_new.append('Mode-Accessoires')
        elif i in ['Handpeeling', 'Nagelfeile','Nagelpflegeset', 'Handgel','Nagellackentferner','Handreinigung', 'Nagelöl' ,'Nagelhärter', 
                 'Handmaske', 'Kunstnägel','Nagelpflegestift', 'Handlotion', 'Nagelbuerste',"Nagelknipser", 'Hand-FuÃŸ-Pflege', 'Nagelgel', 
                 'Nagelsticker', 'Peelinghandschuh', 'Handserum', 'Nagellacktrockner', 'Nagelbalsam', 'Nagelzange', 'Handpflegeset']: 
            type_list_new.append('Handpflege')
        elif i in ["Lippenserum", 'Zahnpasta', 'Lippenpinsel','Zahnaufhellung', 'Lippenfarbe', 'Pflegestift', 'Lippenpeeling']: 
            type_list_new.append('Lippenpflege')   
        elif i in ['Hairstylingset', 'Wattestäbchen', 'Waruftstyler', 'Zahnbürste', "Pudertuch", 'Nagelhautschere', 'Styling-Tools', 
                  'Haarscheren', "Dekolletépflege",'Zerstäuberhülle', 'Puderquaste',  'Epilierer', 'Stylingzubehör']: 
            type_list_new.append('Pflege-Accessoires')
        elif i in ['Fussbad', 'Zehenspreizer', 'Hand-Fuß-Pflege', 'Fußpad', 'Beinspray']:
            type_list_new.append('Fusspflege')
        elif i in ['Körpercreme', 'Körperfluid', 'Körperspray', "Körpermilch", 'Körpermilch', 'Sonnenbalsam','Hals & Dekolletee', 
                   'Waschlotion', 'Öl','Körperseife','Intimpflege','All-in-One Pflege',  'Körpergel', 'Körperbutter','Salbe',  
                    'Gel','Körperschaum','Babycreme','Anti-Cellulite', 'Body Make-up', 'Babyöl',  'Hautpflegemittel']: 
            type_list_new.append('Körperpflege')
        elif i in ['Tonikum', 'Haarbalsam', 'Wachs', 'Haarwasser', 'Föhnlotion', 'Haarbad', 'Haar-Glättung','Haarfestiger']: 
            type_list_new.append('Haarspülung')
        elif i in ["Augenbalsam", 'Augen Roll-on','Augenkompresse', 'Augencreme', 'Augenpatches','Augen-Makeup']: 
            type_list_new.append('Augenpflege')
        elif i in ['Gesichtsdampfbad', "Gesichtsgel", "Gesichtslotion", 'Gesichtsemulsion','Gesichtsbalsam', 'Balsam', 'Anti-Akne Pflege', 
                   'Gesichtsfluid', 'Nachtcreme']: 
            type_list_new.append('Gesichtspflege')
        elif i in ['Badtextilien','Erotik-Accessoires',  'Kinder-Accessoires', 'Ladegerät', 'Raumduft','Spiegel', 
               'Kerze', 'Nahrungsergänzungsmittel','Wimpernpflege','Anhaenger',"Räucherobjekte", "Vitamine", 
               'Handtuch', "Massagezubehör", 'Schwangerschaftsprodukte', 'Küchen-Accessoires', 'Schlafmittel',
               'Sticker', 'Sauna Aufguss', 'Dose', 'Nahrungsmittel', 'Waschmittel', 'Aufbewahrung','Duftobjekte', 
               'Seifenschale',  'Bad-Accessoires']:
            type_list_new.append('Lifestyle-Accessoires')
        elif i in ["Augenbrauenstift", "Augenbrauenschablone",'Wimpernkleber','Wimpernformer', "Wimpernbuerste", "Augenbrauengel", 
                   "Augenbrauenpuder", 'Wimpernfarbe']: 
            type_list_new.append('AugenbrauenWimpernstyling')
        elif i in ['Rasiercreme' ,'Enthaarungsmittel', 'Rasierer', 'Rasiergel', 'After Shave','Enthaarungstools', "Rasierschaum", 'Pre 
                   Shave',]: 
            type_list_new.append('Enthaarungsprodukt')
        elif i in ["Sonnen Make-up", 'Abdeckcreme', 'BB Cream', 'CC Cream', 'Abdeckstift', 'Camouflage']: 
            type_list_new.append('Foundation')
        elif i in ['Eau Fraiche']: 
            type_list_new.append('Eau de Parfum')    
        elif i in ['Hair & Body Wash']: 
            type_list_new.append('Duschgel')   
        elif i in ['Puder', 'Rouge','Bronzer']: 
            type_list_new.append('PuderRougeBronzer') 
        elif i in ['Gesichtsoel', 'Körperöl', 'Serum']: 
            type_list_new.append('SerumÖle') 
        elif i in ['Kajalstift', 'Eyeliner']: 
            type_list_new.append('KajalEyeliner') 
        elif i in ['Körperpeeling', 'Gesichtspeeling']: 
            type_list_new.append('Peeling') 
        elif i in ['Lippenkonturenstift']: 
            type_list_new.append('Lippenstift') 
        elif i in ['Adventskalender','Duftset']: 
            type_list_new.append('Geschenkset')  
        elif i in ['Gesichtswasser','Gesichtsspray']: 
            type_list_new.append('GesichtsSpayWasser')  
        elif i in ['Selbstbräuner','Gesichtsspray', 'Sonnencreme', 'After Sun Pflege','Sonnenhaarspray', 'Sonnenspray']: 
            type_list_new.append('Sonnenprodukte')  
        else: 
            type_list_new.append(i)
        
        return df[column] = type_list_new 
    
    

''' 
this function replaced NaN values by the most frequent value of the column
'''        
def replace_by_mean(data, columns = []):
    for i in columns:
        data[i].fillna(data[i].mean(), inplace = True)

''' 
this gives the unique values of each column of a dataframe
'''   
def unique_val(df):
    for col_names in list(df):
        print("\n" + col_names)
        print(df[col_names].unique(), '\n')
