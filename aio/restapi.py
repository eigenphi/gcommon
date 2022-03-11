# -*- coding: utf-8 -*- 
# created: 2021-06-23
# creator: liguopeng@liguopeng.net
import json
import logging
from functools import partial

import aiohttp
import aiohttp.client_exceptions as ce


logger = logging.getLogger("webclient")


async def get_with_err(url, **kwargs):
    logger.debug("GET send request to: %s", url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            logger.debug("GET %s - %s", url, response.status)
            # declare an error value
            err = None
            if response.status != 200:
                err = ValueError(f"{response.status} {response.reason}")

            try:
                resp = await response.json(), err
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err


async def get(url, **kwargs):
    logger.debug("GET send request to: %s", url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            logger.debug("GET %s - %s", url, response.status)
            try:
                return await response.json()
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err


async def get_text_with_err(url, **kwargs):
    logger.debug("GET send request to: %s", url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            logger.debug("GET %s - %s", url, response.status)
            err = None
            if response.status != 200:
                err = ValueError(f"{response.status} {response.reason}")
                
            try:
                return await response.text(), err
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err

        
async def get_text(url, **kwargs):
    logger.debug("GET send request to: %s", url)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, **kwargs) as response:
            logger.debug("GET %s - %s", url, response.status)

            try:
                return await response.text()
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err


async def post(url, data, **kwargs):
    logger.debug("POST send request to: %s - %s", url, data)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, **kwargs) as response:
            logger.debug("POST %s - %s", url, response.status)

            try:
                return await response.json()
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err


async def post_text(url, data, **kwargs):
    logger.debug("POST send request to: %s - %s", url, data)

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, **kwargs) as response:
            logger.debug("POST %s - %s", url, response.status)
            
            try:
                return await response.text()
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err


async def post_json(url, data, **kwargs):
    logger.debug("POST send request to: %s - %s", url, data.dumps())

    async with aiohttp.ClientSession() as session:
        # session._json_serialize = partial(json.dumps, ensure_ascii=False)
        async with session.post(url, json=data, **kwargs) as response:
            logger.debug("POST %s - %s", url, response.status)
            result = await response.json()
            logger.debug("POST %s - %s", url, result)
            # result = await response.text()
            
            try:
                return result
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err


async def put(url, data, **kwargs):
    logger.debug("PUT send request to: %s - %s", url, data)

    async with aiohttp.ClientSession() as session:
        async with session.put(url, data=data, **kwargs) as response:
            logger.debug("PUT %s - %s", url, response.status)
            
            try:
                return await response.json()
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err


async def delete(url, **kwargs):
    logger.debug("DELETE send request to: %s", url)

    async with aiohttp.ClientSession() as session:
        async with session.delete(url, **kwargs) as response:
            logger.debug("DELETE %s - %s", url, response.status)
            try:
                return await response.json()
            except ce.ClientConnectorError as e:
                logger.error("Connection Error: %s", e.strerror)
                err = ValueError(f"Connection Error: {e.strerror}")
                return None, err
