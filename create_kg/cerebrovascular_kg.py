import rdflib
from util.pg_connection import new_connection
from scrapy_cerebrovascular.model import CerebrovascularDiseases, CDtoC

"""
    使用pg数据库数据创建三元组
"""


class CerebrovascularKG:

    def __init__(self):
        self.g = rdflib.Graph()
        self.engine, self.session = new_connection()
        self.namespace = rdflib.Namespace('https://bit.zust.edu.cn/niai/kg/')

    def select_data(self):
        # data = self.session.query(CerebrovascularDiseases).order_by(CerebrovascularDiseases.rank).all()
        data = self.session.query(CDtoC).order_by(CDtoC.rank).all()
        return data

    def create_rdf(self):
        # 创建类
        rank = rdflib.URIRef(self.namespace + 'class/rank')
        NCTNumber = rdflib.URIRef(self.namespace + 'class/NCTNumber')
        title = rdflib.URIRef(self.namespace + 'class/title')
        acronym = rdflib.URIRef(self.namespace + 'class/acronym')
        status = rdflib.URIRef(self.namespace + 'class/status')
        studyResults = rdflib.URIRef(self.namespace + 'class/studyResults')
        conditions = rdflib.URIRef(self.namespace + 'class/conditions')
        interventions = rdflib.URIRef(self.namespace + 'class/interventions')
        outcomeMeasures = rdflib.URIRef(self.namespace + 'class/outcomeMeasures')
        sponsorCollaborators = rdflib.URIRef(self.namespace + 'class/sponsorCollaborators')
        gender = rdflib.URIRef(self.namespace + 'class/gender')
        age = rdflib.URIRef(self.namespace + 'class/age')
        phases = rdflib.URIRef(self.namespace + 'class/phases')
        enrollment = rdflib.URIRef(self.namespace + 'class/enrollment')
        fundedBys = rdflib.URIRef(self.namespace + 'class/fundedBys')
        studyType = rdflib.URIRef(self.namespace + 'class/studyType')
        studyDesigns = rdflib.URIRef(self.namespace + 'class/studyDesigns')
        otherIDs = rdflib.URIRef(self.namespace + 'class/otherIDs')
        startDate = rdflib.URIRef(self.namespace + 'class/startDate')
        primaryCompletionDate = rdflib.URIRef(self.namespace + 'class/primaryCompletionDate')
        completionDate = rdflib.URIRef(self.namespace + 'class/completionDate')
        firstPosted = rdflib.URIRef(self.namespace + 'class/firstPosted')
        resultsFirstPosted = rdflib.URIRef(self.namespace + 'class/resultsFirstPosted')
        lastUpdatePosted = rdflib.URIRef(self.namespace + 'class/lastUpdatePosted')
        locations = rdflib.URIRef(self.namespace + 'class/locations')
        studyDocuments = rdflib.URIRef(self.namespace + 'class/studyDocuments')
        url = rdflib.URIRef(self.namespace + 'class/url')

        for data in self.select_data():
            if not data.title:
                continue
            d_title = rdflib.URIRef(self.namespace + 'entity/title/' + data.title.replace(' ', '_'))
            if data.rank:
                d_rank = rdflib.URIRef(self.namespace + 'entity/rank/' + str(data.rank).replace(' ', '_'))
                self.g.add((d_title, rank, d_rank))
            if data.nctNumber:
                d_NCTNumber = rdflib.URIRef(self.namespace + 'entity/nctNumber/' + data.nctNumber.replace(' ', '_'))
                self.g.add((d_title, NCTNumber, d_NCTNumber))
            if data.acronym:
                d_acronym = rdflib.URIRef(self.namespace + 'entity/acronym/' + data.acronym.replace(' ', '_'))
                self.g.add((d_title, acronym, d_acronym))
            if data.status:
                d_status = rdflib.URIRef(self.namespace + 'entity/status/' + data.status.replace(' ', '_'))
                self.g.add((d_title, status, d_status))
            if data.studyResults:
                d_studyResults = rdflib.URIRef(
                    self.namespace + 'entity/studyResults/' + data.studyResults.replace(' ', '_'))
                self.g.add((d_title, studyResults, d_studyResults))
            if data.conditions:
                d_conditions = rdflib.URIRef(self.namespace + 'entity/conditions/' + data.conditions.replace(' ', '_'))
                self.g.add((d_title, conditions, d_conditions))
            if data.interventions:
                d_interventions = rdflib.URIRef(
                    self.namespace + 'entity/interventions/' + data.interventions.replace(' ', '_'))
                self.g.add((d_title, interventions, d_interventions))
            if data.outcomeMeasures:
                d_outcomeMeasures = rdflib.URIRef(
                    self.namespace + 'entity/outcomeMeasures/' + data.outcomeMeasures.replace(' ', '_'))
                self.g.add((d_title, outcomeMeasures, d_outcomeMeasures))
            if data.sponsorCollaborators:
                d_sponsorCollaborators = rdflib.URIRef(
                    self.namespace + 'entity/sponsorCollaborators/' + data.sponsorCollaborators.replace(' ', '_'))
                self.g.add((d_title, sponsorCollaborators, d_sponsorCollaborators))
            if data.gender:
                d_gender = rdflib.URIRef(self.namespace + 'entity/gender/' + data.gender.replace(' ', '_'))
                self.g.add((d_title, gender, d_gender))
            if data.age:
                d_age = rdflib.URIRef(self.namespace + 'entity/age/' + data.age.replace(' ', '_'))
                self.g.add((d_title, age, d_age))
            if data.phases:
                d_phases = rdflib.URIRef(self.namespace + 'entity/phases/' + data.phases.replace(' ', '_'))
                self.g.add((d_title, phases, d_phases))
            if data.enrollment:
                d_enrollment = rdflib.URIRef(
                    self.namespace + 'entity/enrollment/' + str(data.enrollment).replace(' ', '_'))
                self.g.add((d_title, enrollment, d_enrollment))
            if data.fundedBys:
                d_fundedBys = rdflib.URIRef(self.namespace + 'entity/fundedBys/' + data.fundedBys.replace(' ', '_'))
                self.g.add((d_title, fundedBys, d_fundedBys))
            if data.studyType:
                d_studyType = rdflib.URIRef(self.namespace + 'entity/studyType/' + data.studyType.replace(' ', '_'))
                self.g.add((d_title, studyType, d_studyType))
            if data.studyDesigns:
                d_studyDesigns = rdflib.URIRef(
                    self.namespace + 'entity/studyDesigns/' + data.studyDesigns.replace(' ', '_'))
                self.g.add((d_title, studyDesigns, d_studyDesigns))
            if data.otherIDs:
                d_otherIDs = rdflib.URIRef(self.namespace + 'entity/otherIDs/' + data.otherIDs.replace(' ', '_'))
                self.g.add((d_title, otherIDs, d_otherIDs))
            if data.startDate:
                d_startDate = rdflib.URIRef(self.namespace + 'entity/startDate/' + data.startDate.replace(' ', '_'))
                self.g.add((d_title, startDate, d_startDate))
            if data.primaryCompletionDate:
                d_primaryCompletionDate = rdflib.URIRef(
                    self.namespace + 'entity/primaryCompletionDate/' + data.primaryCompletionDate.replace(' ', '_'))
                self.g.add((d_title, primaryCompletionDate, d_primaryCompletionDate))
            if data.completionDate:
                d_completionDate = rdflib.URIRef(
                    self.namespace + 'entity/completionDate/' + data.completionDate.replace(' ', '_'))
                self.g.add((d_title, completionDate, d_completionDate))
            if data.firstPosted:
                d_firstPosted = rdflib.URIRef(
                    self.namespace + 'entity/firstPosted/' + data.firstPosted.replace(' ', '_'))
                self.g.add((d_title, firstPosted, d_firstPosted))
            if data.resultsFirstPosted:
                d_resultsFirstPosted = rdflib.URIRef(
                    self.namespace + 'entity/resultsFirstPosted/' + data.resultsFirstPosted.replace(' ', '_'))
                self.g.add((d_title, resultsFirstPosted, d_resultsFirstPosted))
            if data.lastUpdatePosted:
                d_lastUpdatePosted = rdflib.URIRef(
                    self.namespace + 'entity/lastUpdatePosted/' + data.lastUpdatePosted.replace(' ', '_'))
                self.g.add((d_title, lastUpdatePosted, d_lastUpdatePosted))
            if data.locations:
                d_locations = rdflib.URIRef(self.namespace + 'entity/locations/' + data.locations.replace(' ', '_'))
                self.g.add((d_title, locations, d_locations))
            if data.studyDocuments:
                d_studyDocuments = rdflib.URIRef(
                    self.namespace + 'entity/studyDocuments/' + data.studyDocuments.replace(' ', '_'))
                self.g.add((d_title, studyDocuments, d_studyDocuments))
            if data.url:
                d_url = rdflib.URIRef(self.namespace + 'entity/url/' + data.url.replace(' ', '_'))
                self.g.add((d_title, url, d_url))
            self.g.serialize("graph_cn.rdf")


def main():
    ckg = CerebrovascularKG()
    ckg.create_rdf()


if __name__ == '__main__':
    main()
