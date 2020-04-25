# -*- coding: utf-8 -*-
"""
@author: Utkarsh
"""

def isCriminal(sent, info):
    import nltk
    #nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from textblob import TextBlob
    analysis = TextBlob(sent)
    
    criminal_words = "gun, sword, bomb, bullet, ak-47, choke, Abuse, Accomplice, Accused, Accuser, Activists, Adversary, Affect, AFIS, Against, Agency, Aggravated assault, Alarm, Alcohol, Alert, Alias, Alibi, Alienate, Allegation, Ammunition, APB, Appeal, Armed, Arraignment, Arrest, Arsenal, Arson, Art forgery, Assailant, Assault, Attack, Authority, Autopsy,Background check, Backup, Bail, Ballistics, Battery, Beat, Behavior, Behind bars, Belligerence, Big house, Blackmail, Bloodstain, Bombing, Brawl, Breach, Break-in, Breaking and entering, Bribery, Brutality, Burden of proof, Burglary, Bystander, Capture, Caution, Chase, Cheat, Civil, Combat, Commission, Conspiracy, Conviction, Cops, Coroner, Corruption, Counsel, Counterfeit, Court, Credit theft, Crime, Criminal, Criminal justice system, Criminology, Cuffs, Custody, Damage, Danger, Dangerous, Dark side, Data base, Deadly, Deal, Dealings, Death, Deed, Defendant, Defense, Deliberate, Delinquency, Democratic, Denial, Department, Deputy, Detail, Detain, Detection, Detective, Deter, Determination, Deviant, Direct, Dismember, Disobedience, Disorderly, Dispatch, Disregard, Disruption, District attorney, Documents, Dossier, Drill, Drugs, Duty,	Educate, Education, Effect, Elusive, Embezzle, Emergency, Enable, Encumber, Enforce, Entail, Equality, Escape, Ethical, Evasive, Eviction, Evidence, Evil, Examination, Execute, Exonerate, Expert, Explosives, Expunge, Extort, Extradition, Extreme,	Failure, Fairness, Family, Fatality, Fault, FBI, Federal, Felony, Ferocity, Fight, Fighting, Fine, Fingerprint, Firebombing, First-degree, Flee, Footprints, Forbidden, Force, Forensics, Forgery, Formal charge, Frantic, Fraud, Freedom, Full-scale, Fundamental, Furtive,	Good guys, Gory, Government, Grief, Grievance, Guarantee, Guard, Guilty, Gun, Gunrunning, 	Hand-to-hand, Handcuffs, Handle, Harassment, Harm, Harmful, Headquarters, Heinous, Helicopter, Help, Helpful, High-powered rifle, High-profile, Hijack, Hire, Holding cell, Holster, Homicide, Honesty, Honor, Hostage, Hot-line, Humanity,	Identification, Illegal, Immoral, Immunity, Impeach, Impression, Imprison, Improper, Incarceration, Incompetent, Incriminating, Indictment, Influence, Informant, Information, Initiative, Injury, Inmate, Innocence, Innocent, Inquest, Instruct, Integrity, Intelligence, Interests, Interference, International, Interpol, Interpretation, Interrogate, Interrogate, Interstate, Intervention, Interview, Intrastate, Intruder, Invasive, Investigate, Investigation, Irregular, Irresponsible, Issue,	Jail, John Doe, Judge, Judgment, Judicial, Judiciary, Jurisdiction, Jury, Justice, Juvenile,	Kidnapping, Kill, Killer, Kin,	Laboratory, Larceny, Law, Law-abiding, Lawfully, Lawsuit, Lawyer, Leaks, Lease, Legal, Legislation, Legitimate, Lethal, Libel, Liberty, License, Lie detector, Lien, Lieutenant, Limits, Long hours, Lowlife, Loyalty, Lynch, 	Mace, Maintain, Majority, Malice, Malpractice, Manacled, Manslaughter, Marshal, Mayhem, Metal detector, Minor, Minority, Miscreant, Misdemeanor, Missing person, Mission, Model, Money laundering, Moratorium, Motorist, Murder, Murderer, 	National, Negligent, Negotiable, Negotiate, Neighborhood, Network, Nine-one-one, Notation, Notification, Nuisance,	Oath, Obey, Obligation, Offender, Offense, Officer, Official, On-going, Open case, Opinion, Opportunity, Order, Organize, Ownership,	Partner, Partnership, Pathology, Patrol, Pattern, Pedestrian, Peeping Tom, Penalize, Penalty, Perjury, Perpetrator, Petition, Petty theft, Phony, Plainclothes officer, Plea, Plead, Police, Policy, Power, Precedent, Precinct, Preliminary findings, Prevention, Principle, Prior, Prison, Private, Probable cause, Probation, Probation officer, Procedure, Professional, Profile, Prohibit, Proof, Property, Prosecute, Prosecutor, Prostitution, Protection, Protocol, Provision, Public, Punishment,	Quake, Qualification, Quality, Quantify, Quantity, Quarrel, Quell, Question, Quickly, Quirk, Quiver,	Radar, Raid, Rank, Rap sheet, Rape, Reason, Reckless endangerment, Record, Recovery, Recruit, Redress, Reduction, Refute, Register, Regulations, Reinforcement, Reject, Release, Repeal, Reported, Reports, Reprobate, Reputation, Requirement, Resist, Responsibility, Restitution, Restraining order, Restriction, Revenge, Rights, Riot, Robbery, Rogue, Rough, Rules, Rulings,	Sabotage, Safeguard, Sanction, Scene, Sealed record, Search and rescue team, Secret, Seize, Seizure, Selection, Sentence, Sergeant, Serial killer, Seriousness, Services, Sex crimes, Sheriff, Shooting, Shyster, Sighting, Situation, Slashing, Slaying, Smuggling, Sorrow, Speculation, Spying, Squad, Stabbing, Stalking, Statute, Statute of limitation, Stigma, Stipulation, Subdue, Subpoena, Successful, Summons, Supervise, Suppress, Surveillance, Survivor, Suspect, Suspected, Suspicion, Suspicious, Sworn, System,	Tactic, Task force, Terrorism, Testify, Testimony, Theft, Threatening, Three-strikes law, Thwart, Tire-slashing, Torture, Toxicology, Trace, Traffic, Trafficking, Tragedy, Transfer, Trauma, Treatment, Trespass, Trial, Trooper, Trust,	Unacceptable, Unauthorized, Unclaimed, Unconstitutional, Undercover, Underpaid, Understaffed, Unexpected, Unharmed, Uniform, Unintentional, Unit, Unjust, Unknown, Unlawful, Unsolved, Uphold,	Vagrancy, Vandalism, Viable, Vice, Victim, Victimize, Victory, Vigilance, Vigilante, Violate, Violation, Violence, Volunteer, Vow, Voyeurism, Vulnerable,	Wanted poster, Ward, Warning, Warped, Warrant, Watch, Weapon, Will, Wiretap, Wisdom, Witness, Worse, Wrong,	Youth,	Zeal, Zealous"
    criminal_words = criminal_words.replace('\t','')
    criminal_words = criminal_words.lower()
    criminal_words = criminal_words.split(',')
    #criminal_words = criminal_words.replace(' ','')
    
    for i in range(len(criminal_words)):
        criminal_words[i] = criminal_words[i].strip()
    
    criminal_words_stemmed = []
    ps = PorterStemmer()
    for i in range(len(criminal_words)):
        criminal_words_stemmed.append(ps.stem(criminal_words[i]))
    
    tense = info2[0]
    time = info2[1]
    sent = sent.split()
    
    for i in range(len(sent)):
        sent[i] = ps.stem(sent[i])
        
    danger = 0
    future_words = ["let'", "bomb"]
    for i in range(len(tense['future'])):
        future_words.append(tense['future'][i][0])
        
    for s in future_words:
        if s in criminal_words or s in criminal_words_stemmed:
            danger+=10
            
    locations = []
    for i in range(len(tense['location'])):
        locations.append(tense['location'][i][0])
    if danger > 0:
        danger+= (10*len(locations))
    if danger > 0:
        danger+= (5*len(time))
    main_words = len(locations) + len(time) + len(tense['future'])
    if main_words != 0:
        print("Possibility =", danger/(main_words*10)*100, "%")

    if analysis.sentiment.polarity == 0 and danger >= 25:
        return True
    else:
        return False