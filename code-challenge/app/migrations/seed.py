from app import db  
from models import Hero, HeroPower, Power
from datetime import datetime
import random

# generate powers data
power1 = Power(name="super strength", description="gives the wielder super-human strengths")
power2 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
power3 = Power(name="super human senses", description="allows the wielder to use her senses at a super-human level")
power4 = Power(name="super human senses", description="allows the wielder to use her senses at a super-human level")

# generate heroes data
hero1 = Hero(name="Kamala Khan", supername="Ms. Marvel", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero2 = Hero(name="Doreen Green", supername="Squirrel Girl", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero3 = Hero(name="Gwen Stacy", supername="Spider-Gwen", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero4 = Hero(name="Janet Van Dyne", supername="The Wasp", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero5 = Hero(name="Wanda Maximoff", supername="Scarlet Witch", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero6 = Hero(name="Carol Danvers", supername="Captain Marvel", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero7 = Hero(name="Jean Grey", supername="Dark Phoenix", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero8 = Hero(name="Ororo Munroe", supername="Storm", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero9 = Hero(name="Kitty Pryde", supername="Shadowcat", created_at=datetime.utcnow(), updated_at=datetime.utcnow())
hero10 = Hero(name="Elektra Natchios", supername="Elektra", created_at=datetime.utcnow(), updated_at=datetime.utcnow())


# generate hero powers data
strengths = ["Strong", "Weak", "Average"]

heroes = Hero.query.all()
powers = Power.query.all()

# Seed the HeroPower table
for hero in heroes:
  for _ in range(random.randint(1, 3)):
    power = random.choice(powers)
    strength = random.choice(strengths)
    hero_power = HeroPower(hero=hero, power=power, strength=strength, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    db.session.add(hero_power)

# Commit the changes to the database
db.session.commit()


# hero_power1 = HeroPower(strength="High", hero=hero1, power=power1, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
# hero_power2 = HeroPower(strength="Very High", hero=hero1, power=power2, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
# hero_power3 = HeroPower(strength="Medium", hero=hero2, power=power2, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
# hero_power4 = HeroPower(strength="Low", hero=hero2, power=power3, created_at=datetime.utcnow(), updated_at=datetime.utcnow())

# Add the objects and commit to the database
db.session.add_all([power1, power2, power3, hero1, hero2, hero3,  hero4, hero5, hero6, hero7, hero8, hero9, hero10])
db.session.commit()

print("🦸‍♀️ Done seeding!")





# puts "🦸‍♀️ Seeding powers..."
# Power.create([
#   { name: "super strength", description: "gives the wielder super-human strengths" },
#   { name: "flight", description: "gives the wielder the ability to fly through the skies at supersonic speed" },
#   { name: "super human senses", description: "allows the wielder to use her senses at a super-human level" },
#   { name: "elasticity", description: "can stretch the human body to extreme lengths" }
# ])

# puts "🦸‍♀️ Seeding heroes..."
# Hero.create([
#   { name: "Kamala Khan", super_name: "Ms. Marvel" },
#   { name: "Doreen Green", super_name: "Squirrel Girl" },
#   { name: "Gwen Stacy", super_name: "Spider-Gwen" },
#   { name: "Janet Van Dyne", super_name: "The Wasp" },
#   { name: "Wanda Maximoff", super_name: "Scarlet Witch" },
#   { name: "Carol Danvers", super_name: "Captain Marvel" },
#   { name: "Jean Grey", super_name: "Dark Phoenix" },
#   { name: "Ororo Munroe", super_name: "Storm" },
#   { name: "Kitty Pryde", super_name: "Shadowcat" },
#   { name: "Elektra Natchios", super_name: "Elektra" }
# ])

# puts "🦸‍♀️ Adding powers to heroes..."

# strengths = ["Strong", "Weak", "Average"]
# Hero.all.each do |hero|
#   rand(1..3).times do
#     # get a random power
#     power = Power.find(Power.pluck(:id).sample)

#     HeroPower.create!(hero_id: hero.id, power_id: power.id, strength: strengths.sample)
#   end
# end

# puts "🦸‍♀️ Done seeding!"

