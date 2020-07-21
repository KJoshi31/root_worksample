import pytest
from report_engine import ReportEngine

class TestReportEngine:

    @pytest.fixture
    def create_report_engine(self):
        report_engine = ReportEngine()
        return report_engine

    def test_create_report_engine(self, create_report_engine):
        new_re = create_report_engine
        assert isinstance(new_re, ReportEngine) == True