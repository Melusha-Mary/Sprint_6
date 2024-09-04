import pytest
import allure
from data import Answers


class TestHomePage:
    @allure.title('Тест "вопросы и ответы"')
    @pytest.mark.parametrize('question, answer',
                             [(0, Answers.ANSWER_0),
                              (1, Answers.ANSWER_1),
                              (2, Answers.ANSWER_2),
                              (3, Answers.ANSWER_3),
                              (4, Answers.ANSWER_4),
                              (5, Answers.ANSWER_5),
                              (6, Answers.ANSWER_6),
                              (7, Answers.ANSWER_7)])
    def test_questions_and_answer(self, home_page, question, answer):
        home_page.click_on_cookie()
        home_page.scroll_page_to_last_question()
        result = home_page.click_to_question_get_answer(question)
        assert result == answer
