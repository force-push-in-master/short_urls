from typing import Union

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from short_urls.db.db_engine import session_scope
from short_urls.db.repository.transition import TransitionRepository
from short_urls.db.repository.url import UrlRepository

PREFIX = 'urls'
url_router = APIRouter(prefix=f'/{PREFIX}')


class Response(BaseModel):
    result: Union[int, str, None]
    status_code: int


@url_router.post('/')
async def create_short_url(url: str, request: Request) -> Response:
    with session_scope() as session:
        code = UrlRepository.create_short_url(session, url)
    short_url = f'{request.client.host}/urls/{code}'
    return Response(status_code=200, result=short_url)


@url_router.get('/{short_code}')
async def transition_by_code(short_code: str) -> RedirectResponse:
    with session_scope() as session:
        source_url = UrlRepository.get_source_url(session, short_code)
        TransitionRepository.save_transition(session, short_code)
    return RedirectResponse(source_url)


@url_router.get('/{short_code}/stats')
async def transitions_count(short_code: str) -> Response:
    with session_scope() as session:
        count = TransitionRepository.get_count(session, short_code, only_today=True)
    return Response(status_code=200, result=count)


@url_router.put('/{short_code}')
async def transitions_count(short_code: str, url: str) -> Response:
    with session_scope() as session:
        UrlRepository.update_source_url(session, short_code, url)

    return Response(status_code=200)


@url_router.delete('/{short_code}')
async def transitions_count(short_code: str) -> Response:
    with session_scope() as session:
        UrlRepository.delete_by_code(session, short_code)

    return Response(status_code=200)
