from PyPDF2 import PdfReader
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy import displacy



class ResumeParser(object):
    def __init__(self):
        try:
            self.nlp = spacy.load('en_core_web_md')
            self.nlp.max_length = 2000000
        except KeyError as e:
            print(f'Error from loading en_core_web_md{e}')
            
        self.personal_skills = ["communication", "teamwork", "leadership", "problem-solving", "attention to detail", "time management","accountant","erp","critical thinking"]

    def preprocessing(self, sentence):
        stopwords = list(STOP_WORDS)
        doc = self.nlp(sentence)
        clean_tokens = []

        for token in doc:
            if token.text not in stopwords and token.pos_ != 'PUNCT' and token.pos_ != 'SYM' and \
                    token.pos_ != 'SPACE':
                clean_tokens.append(token.lemma_.lower().strip())

        return " ".join(clean_tokens)

    def NER_Visualization(self, text):
        doc = self.nlp(text)
        displacy.render(doc, style="ent", jupyter=True)

    def entity_count(self, text):
        doc = self.nlp(text)
        entity_counts = {}

        for ent in doc.ents:
            entity_counts[ent.label_] = entity_counts.get(ent.label_, 0) + 1

        return entity_counts

    def extract_relevant_entity(self, doc):
        Doc = self.nlp(doc)
        for ent in Doc.ents:
            print(ent.text, ent.label_)

    def identify_personal_skills(self, text):
        doc = self.nlp(text)
        found_skills = set()

        for token in doc:
            if token.text.lower() in self.personal_skills:
                found_skills.add(token.text.lower())

        return found_skills

    def evaluate(self, skillSet):
      evaluation = 0
      for item in skillSet:
        if(item in self.personal_skills):
          evaluation += 1

      percentage = evaluation/len(self.personal_skills) * 100
      
      return percentage
