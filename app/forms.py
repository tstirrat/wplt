from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, BooleanField, SelectMultipleField, RadioField
from wtforms.validators import InputRequired, NumberRange
import requests

professions = [
    'Alchemy',
    'Blacksmithing',
    'Cooking',
    'Enchanting',
    'Engineering',
    'Inscription',
    'Jewelcrafting',
    'Leatherworking',
    'Mining',
    'Tailoring']

# Fetch server list
response = requests.get("https://api.nexushub.co/wow-classic/v1/servers/full/")
responseJson = response.json()

servers = dict()
for line in responseJson:
    servers[line["slug"]] = line["name"]

class UserInputForm(FlaskForm):
    server = SelectField(u'Server',
        default='old-blanchy',
        choices=[(slug, name) for slug, name in servers.items()])
    faction = SelectField(u'Faction',
        default='alliance',
        choices=[('alliance', 'Alliance'), ('horde', "Horde")])
    profession = SelectField(u'Profession',
        default='Inscription',
        choices=[(profession, profession) for profession in professions])
    startSkill = IntegerField(u'Starting skill',
        default=380,
        validators=[InputRequired(),
                    NumberRange(min=1, max=450)])
    targetSkill = IntegerField(u'Target skill',
        default=450,
        validators=[InputRequired(),
                    NumberRange(min=2, max=450)])
    phase = SelectField(u'Phase',
        default='0',
        choices=[('1', '1')])
    calculate = SubmitField('Calculate')
    includeVendor = BooleanField(u'Vendor', default="checked")
    includeCraftToken = BooleanField(u'CraftToken', default="checked")
    includeVendorLimited = BooleanField(u'VendorLimited', default="checked")
    includeDiscovery = BooleanField(u'Discovery', default="checked")
    includeDrop = BooleanField(u'Drop')
    includeQuest = BooleanField(u'Quest')
    includeReputation = BooleanField(u'Reputation')
    includeSeasonal = BooleanField(u'Seasonal')
    blacksmithingSchool = RadioField(u'School:',
        choices=[("None", "None"),
                ("Armorsmithing", "Armorsmithing"),
                ("Weaponsmithing", "Weaponsmithing")],
        default="None")
    engineeringSchool = RadioField(u'School:',
        choices=[("None", "None"),
                ("Gnomish", "Gnomish"),
                ("Goblin", "Goblin")],
        default="None")
    leatherworkingSchool = RadioField(u'School:',
        choices=[("None", "None"),
                 ("Dragonscale", "Dragonscale"),
                 ("Elemental", "Elemental"),
                 ("Tribal", "Tribal")],
        default="None")
    enchantingRods = BooleanField(u'Include enchanting rods', default="checked")